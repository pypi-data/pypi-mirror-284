import atexit
import signal
import time
import uuid
from datetime import datetime
from threading import Event
from typing import Any, Dict, List, Optional, Callable
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor

import requests

from src.utils import get_device_data, send_event_to_server, process_dlq, generate_session, get_server_details


class CarterAnalytics:
    _shutdown_event: Event = Event()
    _instances: List[Dict[str, Any]] = []
    _initialized: bool = False
    _event_queue: Queue = Queue()
    _event_queue_dlq: Queue = Queue()
    executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=2)
    session: Dict[str, Any] = {}
    _server_details: Dict[str, Any] = get_server_details()
    __version: str = None

    @classmethod
    def initialize(cls, configurations: List[Dict[str, Any]], **kwargs) -> None:
        if not configurations:
            raise ValueError('At least one instance configuration is required for initialization.')

        authenticated_configs, errors = cls._authenticate(configurations)

        if not authenticated_configs:
            raise ValueError(f'Configurations did not pass authentication. Errors: {errors}')

        cls.__version = kwargs.get('version')
        cls._instances.extend(configurations)
        cls._initialized = True
        print('Carter Analytics Initialized')
        print('Instances:', cls._instances)

    @classmethod
    def _authenticate(cls, configs: List[Dict[str, Any]]) -> tuple[List[Dict[str, Any]], List[str]]:
        authenticated_configs = []
        errors = []
        for config in configs:
            try:
                if cls._validate_config(config):  # Add validation before API call (optional)
                    response = requests.post(url='https://your_api_endpoint', json={'api_key': config.get('api_key')})
                    response.raise_for_status()
                    if response.json().get('success', False):  # Assuming success key in response
                        authenticated_configs.append(config)
                    else:
                        errors.append(f"API validation failed for config: {config}")
                else:
                    errors.append(f"Configuration validation failed: {config}")
            except requests.exceptions.RequestException as e:
                errors.append(f"Error authenticating with config: {config}, Error: {e}")

        return authenticated_configs, errors

    @staticmethod
    def _validate_config(config: Dict[str, Any]) -> bool:
        # Implement your configuration validation logic here (optional)
        # This example checks for a required 'api_key' field
        return 'api_key' in config

    @classmethod
    def publish(cls, event_data: Dict[str, Any]) -> None:
        if not cls._initialized:
            raise Exception('CarterAnalytics SDK has not been initialized. Please initialize before publishing events.')

        transformed_meta_parameters = cls._generate_meta_parameters(event_data.get('meta_parameters', {}))

        event_data['meta_parameters'] = transformed_meta_parameters
        cls._event_queue.put(event_data)

    @classmethod
    def publish_init_event(cls):
        if not cls.session:
            cls.session = generate_session()
        data = {
            "event": "init",
        }
        cls.publish(data)

    @classmethod
    def _generate_meta_parameters(cls, meta_parameters: Dict[str, Any] | None, **kwargs) -> Dict[str, Any]:
        user_device_details = {}
        if 'user_agent' in meta_parameters:
            user_device_details.update(get_device_data(meta_parameters.get('user_agent')))
        if 'ip_address' in meta_parameters:
            user_device_details.update({"ip_address": meta_parameters.get('ip_address')})

        meta_parameters = {
            "session_id": cls.session.get('id'),
            "device": user_device_details,
            "server": {
                    "ip_address": "",
                    "platform": cls._server_details,
                    "sdk_details": {
                        "version": cls.__version
                    }
                },
            "is_capi_server": True,
            "timestamp": time.time(),
            "referrer": meta_parameters.get('referrer')
        }

        return meta_parameters

    @classmethod
    def worker(cls, publish_func: Callable, queue: Queue, queue_dlq: Queue | None, **kwargs) -> None:
        while not cls._shutdown_event.is_set():
            try:
                event_data = queue.get(timeout=1)
            except Empty:
                continue
            try:
                publish_func(event_data, **kwargs)
            except Exception as e:
                if not queue_dlq:
                    print(f"Failed to send event even after retries... {event_data}")
                    return
                queue_dlq.put(event_data)
            finally:
                cls._event_queue.task_done()  # Ensure we don't block the queue

    @classmethod
    def start_background_worker(cls):
        if not cls._initialized:
            raise Exception("CarterAnalytics SDK must be initialized before starting the background worker.")

        for _ in range(2):  # Adjust number of workers as needed
            cls.executor.submit(cls.worker, send_event_to_server, cls._event_queue, cls._event_queue_dlq,
                                **{'config': cls._instances})
            cls.executor.submit(cls.worker, process_dlq, cls._event_queue_dlq, None,
                                **{'config': cls._instances})

    @classmethod
    def shutdown(cls):
        print("received shutdown event")
        cls._shutdown_event.set()  # Signal all workers to exit
        cls.executor.shutdown(wait=True)  # Wait for all workers to finish


atexit.register(CarterAnalytics.shutdown)


# Signal handler function
def handle_sigint(signum, frame):
    print("SIGINT received, shutting down...")
    CarterAnalytics.shutdown()


signal.signal(signal.SIGINT, handle_sigint)

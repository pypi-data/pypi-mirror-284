import platform
import time
import uuid
from datetime import datetime, timedelta

import requests
from typing import Any, Dict
from tenacity import retry, stop_after_attempt, wait_incrementing
import user_agents


def get_device_data(user_agent: str) -> Dict[str, str]:
    ua_parser = user_agents.parse(user_agent)

    device_data = {
        "category": ua_parser.device.family,
        "brand": ua_parser.device.brand,
        "platform": ua_parser.os.family,
    }

    return device_data


def send_event_to_server(event_data: dict, **kwargs) -> None:
    """
    Sends the given event data to the analytics server.
    Retries on failure with a fixed wait strategy.

    :param event_data: The event data to be sent.
    :return: True if the event was successfully sent, False otherwise.
    """
    try:
        # response = requests.post("https://your-analytics-endpoint.com/event", json=event_data)
        # response.raise_for_status()  # This will raise an exception for 4XX and 5XX responses
        configs = kwargs.get('config')
        for config in configs:
            print("data", event_data)
    except Exception as e:
        print(f"Failed to send event due to {e}")
        raise e  # Re-raise the exception to handle at function call


@retry(stop=stop_after_attempt(3), wait=wait_incrementing(start=10000, increment=10000))
def process_dlq(event_data: dict, **kwargs) -> None:
    send_event_to_server(event_data, config=kwargs.get('config'))


def generate_session() -> Dict[str, str]:
    """
    Generates a session dictionary containing a unique ID and its expiration time.

    Returns:
      Dict[str, str]: A dictionary with keys "session_id" and "expires_at".
    """
    # Generate random session ID
    random_part = uuid.uuid4().hex[:8]
    timestamp_part = str(int(time.time() * 1000))[1:]  # Remove leading '1'
    session_id = f"{random_part}-{timestamp_part}"

    # Calculate expiration time (current time + 30 days)
    expiration_time = (datetime.now() + timedelta(days=30))

    return {
      "id": session_id,
      "expires_at": expiration_time
    }


def get_server_details() -> Dict[str, Any]:
    """
    Retrieves information about the server platform and OS.
    """
    return {
        "OS": platform.system(),  # Operating system (e.g., 'Windows', 'Linux', 'Darwin')
        "version": platform.version(),  # OS version
        "architecture": platform.machine(),  # System architecture (e.g., 'x86_64')
    }

from typing import Any, List, Dict, Optional
from src.core import CarterAnalytics as CarterAnalyticsWrapper
from src.events import EventPublisher
from src.models import (ProductItem, CartItem, CheckoutStartEvent, CheckoutCompletedEvent, CheckoutCancelledEvent,
                        Address, Discount)

VERSION = '0.1.0'


class CarterAnalyticsClient(EventPublisher):
    @staticmethod
    def initialize(configurations: List[Dict[str, Any]]) -> None:
        """
        Initializes the Carter Analytics SDK with given configurations.
        """
        if not isinstance(configurations, list) or not all(isinstance(item, dict) for item in configurations):
            raise TypeError("configurations must be a list of dictionaries.")
        CarterAnalyticsWrapper.initialize(configurations, version=VERSION)
        # trigger init event
        CarterAnalyticsWrapper.publish_init_event()
        CarterAnalyticsWrapper.start_background_worker()

    @staticmethod
    def publish(event_data: dict[str, Any]) -> None:
        """
        Publishes an event with the given event data, optionally enhanced with details extracted from
        the user's request.

        :param event_data: The event data to be sent.
        :param request: The user's request object, from which location and device details can be extracted.
        """
        CarterAnalyticsWrapper.publish(event_data)


# Directly exposing the CarterAnalyticsClient under the name `carter_analytics_client` for import
carter_analytics_client = CarterAnalyticsClient

__all__ = [
    "VERSION",
    "carter_analytics_client",
    "ProductItem",
    "CartItem",
    "Address",
    "Discount",
    "CheckoutStartEvent",
    "CheckoutCompletedEvent",
    "CheckoutCancelledEvent",
]

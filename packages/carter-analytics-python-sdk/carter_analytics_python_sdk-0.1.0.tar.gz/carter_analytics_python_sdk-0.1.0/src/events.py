from enum import Enum, auto
from typing import Dict, List, Any, Optional
from .models import (ProductItem, CartItem, CheckoutStartEvent, CheckoutCompletedEvent,
                     CheckoutCancelledEvent)

# Define a type alias for clarity
EventProperties = Dict[str, Any]


class EventType(Enum):
    PAGE_VIEW = auto()
    SEARCH = auto()
    SIGN_UP = auto()
    LOGIN = auto()
    PRODUCT_VIEW = auto()
    PRODUCT_CLICK = auto()
    PRODUCT_IMPRESSION = auto()
    ADD_TO_CART = auto()
    REMOVE_FROM_CART = auto()
    UPDATE_CART = auto()
    VIEW_CART = auto()
    CHECKOUT_START = auto()
    CHECKOUT_COMPLETED = auto()
    CHECKOUT_CANCELLED = auto()


class EventPublisher:
    # generic event publishing function
    @staticmethod
    def publish_event(event_type: EventType, event_properties: Dict[str, Any] = None,
                      user_properties: Dict[str, Any] = None) -> None:
        from src.core import CarterAnalytics
        event_data = {
            'event': event_type.name.lower(),
            'event_properties': event_properties if event_properties else {},
            'user_properties': user_properties if user_properties else {}
        }

        CarterAnalytics.publish(event_data)

    # Core Events
    @staticmethod
    def publish_page_view(request: Optional[Any] = None) -> None:
        EventPublisher.publish_event(EventType.PAGE_VIEW, request)

    @staticmethod
    def publish_search(query: str) -> None:
        EventPublisher.publish_event(EventType.SEARCH, {'query': query})

    @staticmethod
    def publish_signup(method: str, user_id: str) -> None:
        EventPublisher.publish_event(EventType.SIGN_UP, {'method': method, 'user_id': user_id})

    @staticmethod
    def publish_login(method: str, user_id: str) -> None:
        EventPublisher.publish_event(EventType.LOGIN, {'method': method, 'user_id': user_id})

    # Product Interactions
    @staticmethod
    def publish_product_view(product: ProductItem) -> None:
        EventPublisher.publish_event(EventType.PRODUCT_VIEW, product.to_dict())

    @staticmethod
    def publish_product_click(product: ProductItem) -> None:
        EventPublisher.publish_event(EventType.PRODUCT_CLICK, product.to_dict())

    @staticmethod
    def publish_product_impression(product: ProductItem) -> None:
        EventPublisher.publish_event(EventType.PRODUCT_IMPRESSION, product.to_dict())

    # Shopping Cart Actions
    @staticmethod
    def publish_add_to_cart(cart_amount: float, currency: str,
                            cart_items: List[CartItem]) -> None:
        EventPublisher.publish_event(EventType.ADD_TO_CART, {
            'cart_amount': cart_amount,
            'currency': currency,
            'cart_items': [item.to_dict() for item in cart_items]
        })

    @staticmethod
    def publish_remove_from_cart(cart_amount: float, currency: str,
                                 cart_items: List[CartItem]) -> None:
        EventPublisher.publish_event(EventType.REMOVE_FROM_CART, {
            'cart_amount': cart_amount,
            'currency': currency,
            'cart_items': [item.to_dict() for item in cart_items]
        })

    @staticmethod
    def publish_update_cart(cart_amount: float, currency: str,
                            cart_items: List[CartItem]) -> None:
        EventPublisher.publish_event(EventType.UPDATE_CART, {
            'cart_amount': cart_amount,
            'currency': currency,
            'cart_items': [item.to_dict() for item in cart_items]
        })

    @staticmethod
    def publish_view_cart(cart_amount: float, currency: str,
                          cart_items: List[CartItem]) -> None:
        EventPublisher.publish_event(EventType.VIEW_CART, {
            'cart_amount': cart_amount,
            'currency': currency,
            'cart_items': [item.to_dict() for item in cart_items]
        })

    # Checkout Process
    @staticmethod
    def publish_checkout_start(event: CheckoutStartEvent) -> None:
        EventPublisher.publish_event(EventType.CHECKOUT_START, event.to_dict())

    @staticmethod
    def publish_checkout_completed(event: CheckoutCompletedEvent) -> None:
        EventPublisher.publish_event(EventType.CHECKOUT_COMPLETED, event.to_dict())

    @staticmethod
    def publish_checkout_cancelled(event: CheckoutCancelledEvent) -> None:
        EventPublisher.publish_event(EventType.CHECKOUT_CANCELLED, event.to_dict())

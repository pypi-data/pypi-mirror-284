from dataclasses import dataclass
from typing import Optional, List


@dataclass
class ProductItem:
    id: str
    price: float
    currency: str
    title: str
    sku_id: Optional[str] = None
    image_url: Optional[str] = None
    product_url: Optional[str] = None
    affiliation: Optional[str] = None
    product_category_1: Optional[str] = None
    product_category_2: Optional[str] = None
    product_category_3: Optional[str] = None
    product_category_4: Optional[str] = None
    product_category_5: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class CartItem:
    id: str
    price: float
    currency: str
    title: str
    quantity: int = 1
    discount: float = 0.0
    # Optional fields
    sku_id: Optional[str] = None
    image_url: Optional[str] = None
    product_url: Optional[str] = None
    affiliation: Optional[str] = None
    product_category_1: Optional[str] = None
    product_category_2: Optional[str] = None
    product_category_3: Optional[str] = None
    product_category_4: Optional[str] = None
    product_category_5: Optional[str] = None

    def __post_init__(self):
        # If sku_id is not provided, it should default to id
        if not self.sku_id:
            self.sku_id = self.id

    @property
    def amount(self) -> float:
        # The final amount is price * quantity - discount
        return max(self.price * self.quantity - self.discount, 0)  # Ensuring the amount never goes negative

    def to_dict(self) -> dict:
        # Convert the dataclass to a dictionary, and include the calculated amount
        data = self.__dict__
        data['amount'] = self.amount  # Insert the calculated amount
        return data


@dataclass
class Address:
    address_line_1: str
    city: str
    province: str
    country: str
    address_line_2: Optional[str] = None
    province_code: Optional[str] = None
    country_code: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class Discount:
    application: str  # 'AUTOMATIC' or 'MANUAL'
    amount: float
    code: Optional[str] = None
    target: Optional[str] = None  # 'shipping' or 'line_item'

    def to_dict(self) -> dict:
        return self.__dict__


@dataclass
class CheckoutStartEvent:
    token: str
    amount: float
    currency: str
    items: List[CartItem]
    billing_address: List[Address]
    shipping_address: List[Address]
    discounts: List[Discount]
    delivery_method: str
    payment_method: str

    def to_dict(self) -> dict:
        return {
            "token": self.token,
            "amount": self.amount,
            "currency": self.currency,
            "items": [item.to_dict() for item in self.items],
            "billing_address": [address.to_dict() for address in self.billing_address],
            "shipping_address": [address.to_dict() for address in self.shipping_address],
            "discounts": [discount.to_dict() for discount in self.discounts],
            "delivery_method": self.delivery_method,
            "payment_method": self.payment_method,
        }


@dataclass
class CheckoutCompletedEvent:
    token: str
    order_id: str
    amount: float
    currency: str
    items: List[CartItem]
    billing_address: List[Address]
    shipping_address: List[Address]
    discounts: List[Discount]
    delivery_method: str
    payment_method: str
    transaction_id: str

    def to_dict(self) -> dict:
        return {
            "token": self.token,
            "order_id": self.order_id,
            "amount": self.amount,
            "currency": self.currency,
            "items": [item.to_dict() for item in self.items],
            "billing_address": [address.to_dict() for address in self.billing_address],
            "shipping_address": [address.to_dict() for address in self.shipping_address],
            "discounts": [discount.to_dict() for discount in self.discounts],
            "delivery_method": self.delivery_method,
            "payment_method": self.payment_method,
            "transaction_id": self.transaction_id,
        }


@dataclass
class CheckoutCancelledEvent:
    token: str
    reason: str
    amount: float
    currency: str
    items: List[CartItem]
    billing_address: List[Address]
    shipping_address: List[Address]
    discounts: List[Discount]
    delivery_method: str
    payment_method: str
    transaction_id: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "token": self.token,
            "reason": self.reason,
            "amount": self.amount,
            "currency": self.currency,
            "items": [item.to_dict() for item in self.items],
            "billing_address": [address.to_dict() for address in self.billing_address],
            "shipping_address": [address.to_dict() for address in self.shipping_address],
            "discounts": [discount.to_dict() for discount in self.discounts],
            "delivery_method": self.delivery_method,
            "payment_method": self.payment_method,
            "transaction_id": self.transaction_id,
        }

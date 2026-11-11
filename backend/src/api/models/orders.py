from dataclasses import dataclass
from enum import Enum
from pydantic import BaseModel
from decimal import Decimal


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: Decimal

@dataclass
class Order:
    customer_id: str
    store_id: str
    items: list[OrderItem]
    total: Decimal
    status: OrderStatus

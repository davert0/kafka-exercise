from enum import Enum


class EventType(str, Enum):
    ORDER_CREATED = "ORDER_CREATED"
    ORDER_PAID = "ORDER_PAID"
    ORDER_CANCELED = "ORDER_CANCELED"

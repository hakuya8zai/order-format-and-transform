from abc import ABC, abstractmethod
from asiaYo.order.schemas.order_schemas import OrderSchema


class OrderTransformer(ABC):
    @abstractmethod
    def transform(order) -> OrderSchema:
        pass


class CurrencyTransformer(OrderTransformer):
    @staticmethod
    def transform(order: OrderSchema):
        if order.currency == "USD":
            order_price = int(order.price)
            order_price *= 31
            order.price = str(order_price)
            order.currency = "TWD"
        return order

from abc import ABC, abstractmethod
from asiaYo.order.schemas.order_schemas import OrderSchema


class OrderValidator(ABC):
    @abstractmethod
    def validate(order: OrderSchema) -> None:
        pass


class NameValidator(OrderValidator):
    @staticmethod
    def validate(order: OrderSchema) -> None:
        if any(not char.isascii() for char in order.name):
            raise ValueError("Name contains non-English characters")
        if not all(word[0].isupper() for word in order.name.split()):
            raise ValueError("Name is not capitalized")


class CurrencyValidator(OrderValidator):
    @staticmethod
    def validate(order: OrderSchema) -> None:
        if order.currency not in ["TWD", "USD"]:
            raise ValueError("Currency format is wrong")


class PriceValidator(OrderValidator):
    @staticmethod
    def validate(order: OrderSchema) -> None:
        price_int = int(order.price)
        if price_int > 2000:
            raise ValueError("Price is over 2000")

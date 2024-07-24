from abc import ABC, abstractmethod
from asiaYo.order.schemas.order_schemas import OrderSchema


class OrderValidator(ABC):
    @abstractmethod
    def validate(self, order: OrderSchema) -> None:
        pass


class NameValidator(OrderValidator):
    def validate(self, order: OrderSchema) -> None:
        if any(char.isdigit() for char in order.name):
            raise ValueError("Name contains non-English characters")
        if not all(word[0].isupper() for word in order.name.split()):
            raise ValueError("Name is not capitalized")

class CurrencyValidator(OrderValidator):
    def validate(self, order: OrderSchema) -> None:
        if order.currency not in ['TWD', 'USD']:
            raise ValueError("Currency is not supported")

class PriceValidator(OrderValidator):
    def validate(self, order: OrderSchema) -> None:
        if int(order.price) > 2000:
            raise ValueError("Price is over 2000")

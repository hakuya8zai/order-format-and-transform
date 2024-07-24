from abc import ABC, abstractmethod
from asiaYo.order.schemas.order_schemas import OrderSchema

class OrderTransformer(ABC):
    @abstractmethod
    def transform(self, order) -> OrderSchema:
        pass

class CurrencyTransformer(OrderTransformer):
    def transform(self, order : OrderSchema):
        if order.currency == 'USD':
            price = int(order.price)
            price *= 31
            order.price = str(price)
            order.currency = 'TWD'
        return order
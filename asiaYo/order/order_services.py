from asiaYo.order.utils.validators.order_validator import NameValidator, PriceValidator, CurrencyValidator
from asiaYo.order.utils.transformers.order_transformer import  CurrencyTransformer
from asiaYo.order.schemas.order_schemas import OrderSchema


class OrderService:
    def __init__ (self):
        self.transformers = [CurrencyTransformer()]
        self.validators = [NameValidator(),CurrencyValidator(), PriceValidator()]

    def process_order(self, order: OrderSchema) -> OrderSchema:
        for transformer in self.transformers:
            order = transformer.transform(order)
        for validator in self.validators:
            validator.validate(order)
        return order

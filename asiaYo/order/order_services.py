from typing import List
from asiaYo.order.schemas.order_schemas import OrderSchema
from asiaYo.order.utils.transformers.order_transformer import OrderTransformer
from asiaYo.order.utils.validators.order_validator import OrderValidator


class OrderService:
    def __init__(
        self, transformers: List[OrderTransformer], validators: List[OrderValidator]
    ):
        self.transformers = transformers
        self.validators = validators

    def process_order(self, order: OrderSchema) -> OrderSchema:
        for transformer in self.transformers:
            order = transformer.transform(order)
        for validator in self.validators:
            validator.validate(order)
        return order

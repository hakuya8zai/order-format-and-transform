# dependency.py
from fastapi import Depends
from typing import List
from asiaYo.order.utils.transformers.order_transformer import CurrencyTransformer
from asiaYo.order.utils.validators.order_validator import (
    NameValidator,
    PriceValidator,
    CurrencyValidator,
)
from asiaYo.order.order_services import OrderService


def get_transformers() -> List:
    return [CurrencyTransformer()]


def get_validators() -> List:
    return [NameValidator(), CurrencyValidator(), PriceValidator()]


def get_order_service(
    transformers=Depends(get_transformers),
    validators=Depends(get_validators),
) -> OrderService:
    return OrderService(transformers, validators)

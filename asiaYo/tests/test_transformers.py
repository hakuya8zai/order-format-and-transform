from asiaYo.order.utils.transformers.order_transformer import CurrencyTransformer
from asiaYo.order.schemas.order_schemas import OrderSchema, AddressSchema


def test_transformer_success_with_TWD():
    transformer = CurrencyTransformer()
    order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    result = transformer.transform(order)
    assert result == order


def test_transform_success_with_USD():
    transformer = CurrencyTransformer()
    EXCHANGE_RATE = 31
    order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="500",
        currency="USD",
    )
    expected_price = int(order.price) * EXCHANGE_RATE
    result = transformer.transform(order)
    assert int(result.price) == expected_price
    assert result.currency == "TWD"


def test_transform_fail_with_JPY():
    transformer = CurrencyTransformer()
    order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="500",
        currency="JPY",
    )
    result = transformer.transform(order)
    assert result == order

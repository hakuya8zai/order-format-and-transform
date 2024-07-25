import pytest
from asiaYo.order.utils.validators.order_validator import (
    NameValidator,
    PriceValidator,
    CurrencyValidator,
)
from asiaYo.order.schemas.order_schemas import OrderSchema, AddressSchema


def test_name_valid():
    mock_order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    validator = NameValidator()
    assert validator.validate(mock_order) is None


def test_name_starts_without_capital():
    mock_order = OrderSchema(
        id="A0000001",
        name="test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    validator = NameValidator()
    with pytest.raises(ValueError) as exception_info:
        validator.validate(mock_order)
    assert "Name is not capitalized" in str(exception_info.value)


def test_name_with_non_english_characters():
    mock_order = OrderSchema(
        id="A0000001",
        name="測試",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    validator = NameValidator()
    with pytest.raises(ValueError) as exception_info:
        validator.validate(mock_order)
    assert "Name contains non-English characters" in str(exception_info.value)


def test_price_valid():
    mock_order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    validator = PriceValidator()
    assert validator.validate(mock_order) is None


def test_price_exceeds_limit():
    mock_order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="2001",
        currency="TWD",
    )
    validator = PriceValidator()
    with pytest.raises(ValueError) as exception_info:
        validator.validate(mock_order)
    assert "Price is over 2000" in str(exception_info.value)


def test_currency_valid():
    mock_order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="TWD",
    )
    validator = CurrencyValidator()
    assert validator.validate(mock_order) is None


def test_currency_wrong_format():
    mock_order = OrderSchema(
        id="A0000001",
        name="Test",
        address=AddressSchema(
            city="taipei-city", district="da-an-district", street="fuxing-south-road"
        ),
        price="1000",
        currency="JPY",
    )
    validator = CurrencyValidator()
    with pytest.raises(ValueError) as exception_info:
        validator.validate(mock_order)
    assert "Currency format is wrong" in str(exception_info.value)

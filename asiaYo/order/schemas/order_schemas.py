from pydantic import BaseModel, field_validator


class AddressSchema(BaseModel):
    city: str
    district: str
    street: str


class OrderSchema(BaseModel):
    id: str
    name: str
    address: AddressSchema
    price: str
    currency: str

    @field_validator("price")
    def check_price_is_numeric(cls, value):
        try:
            int(value)
        except ValueError:
            raise ValueError("Price must be a numeric value.")
        return value

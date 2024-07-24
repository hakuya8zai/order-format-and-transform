from pydantic import BaseModel

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
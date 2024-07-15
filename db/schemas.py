"""
Pydantic schema equivalents of Sqlalchemy objects
"""
from pydantic import BaseModel


class Article(BaseModel):
    sku: str
    name: str
    price: float

    class Config:
        # To let pydantic automatically handle sqlalchemy objects
        from_attributes = True


class Order(BaseModel):
    tracking_number: str
    carrier: str
    sender_address: str
    receiver_address: str
    status: str

    class Config:
        # To let pydantic automatically handle sqlalchemy objects
        from_attributes = True

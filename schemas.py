from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    location: str

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    customer_id: int
    class Config:
        from_attributes = True

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    product_id: int
    class Config:
        from_attributes = True

class TransactionBase(BaseModel):
    customer_id: int
    product_id: int

class TransactionCreate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    transaction_id: int
    purchase_date: datetime
    class Config:
        from_attributes = True

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from database import Base
import datetime

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    purchase_date = Column(DateTime, default=datetime.datetime.utcnow)

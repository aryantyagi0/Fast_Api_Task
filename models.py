from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=True)
    address = Column(String, nullable=True)
    age = Column(Integer, nullable=True)       # make sure this exists
    city = Column(String, nullable=True)       # make sure this exists
    created_at = Column(DateTime, nullable=False)

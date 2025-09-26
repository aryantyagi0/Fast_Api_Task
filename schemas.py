from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# Base user model (shared fields)
class UserBase(BaseModel):
    name: str
    email: EmailStr


# Model for creating a new user
class UserCreate(UserBase):
    phone_number: Optional[str] = None
    address: Optional[str] = None
    age: Optional[int] = None  
    city: Optional[str] = None   # <-- added


# Model for updating a user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    age: Optional[int] = None  
    city: Optional[str] = None   # <-- added


# Model for response
class UserOut(UserBase):
    id: int
    phone_number: Optional[str] = None
    address: Optional[str] = None
    age: Optional[int] = None  
    city: Optional[str] = None   # <-- added
    created_at: datetime

    model_config = {
        "from_attributes": True  
    }

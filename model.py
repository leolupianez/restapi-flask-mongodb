import uuid
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    first_name: str
    middle_name: str
    last_name: str
    password: str
    phone: str
    session_token: str
    created_datetime: datetime
    updated_datetime: datetime


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    updated_datetime: datetime = datetime.now()

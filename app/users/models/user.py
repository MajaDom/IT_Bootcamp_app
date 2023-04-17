"""Model for User"""
from uuid import uuid4
from datetime import date

from sqlalchemy import Column, String, Date, Boolean, Integer

from app.db import Base


class User(Base):
    """Base Model for User"""
    __tablename__ = "users"
    id = Column(String(50), primary_key=True, default=uuid4)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    password_hashed = Column(String(100))
    date_subscribed = Column(Date(), default=date.today())
    is_active = Column(Boolean)
    is_superuser = Column(Boolean, default=False)
    verification_code = Column(Integer(), nullable=True)

    # TODO: class_id, user_type_id relationships will be added

    def __init__(self, first_name: str, last_name: str, email: str, password_hashed: str,
                 date_subscribed: str = date.today(), is_active: bool = True, is_superuser: bool = False,
                 verification_code: int = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hashed = password_hashed
        self.date_subscribed = date_subscribed
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.verification_code = verification_code

"""User Schemas module"""
from typing import Optional
from pydantic import BaseModel, UUID4, EmailStr


class UserSchema(BaseModel):
    """Base schema for User"""
    id: UUID4
    first_name: str
    last_name: str
    email: str
    password_hashed: str
    is_active: bool
    is_superuser: bool
    verification_code: Optional[int]

    class Config:
        """Configuration Class"""
        orm_mode = True


class UserSchemaIn(BaseModel):
    """Base User schema for input"""
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    class Config:
        """Configuration Class"""
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "dummy@gmail.com",
                "password": "password",
            }
        }


class UserLoginSchema(BaseModel):
    """Login User Schema"""
    email: str
    password: str

    class Config:
        """Configuration Class"""
        schema_extra = {
            "example": {
                "email": "dummy@gmail.com",
                "password": "password"
            }
        }

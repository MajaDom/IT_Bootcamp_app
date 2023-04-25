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


class UserSchemaOut(BaseModel):
    """User Out schema"""
    id: UUID4
    first_name: str
    last_name: str
    email: str
    is_active: bool
    is_superuser: bool
    verification_code: Optional[int]

    class Config:
        """Configuration Class"""
        orm_mode = True


class UserRegistrationSchema(BaseModel):
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


class ChangePasswordSchema(BaseModel):
    """User schema for password change"""
    code: int
    new_password: str
    repeat_password: str

    class Config:
        """Configuration Class"""
        schema_extra = {
            "example": {
                "code": 123456,
                "new_password": "new_password",
                "repeat_password": "repeat_password"
            }
        }


class UserUpdateSchema(BaseModel):
    """User schema for update"""
    first_name: str
    last_name: str
    email: str

    class Config:
        """Configuration Class"""
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "dummy@gmail.com"
            }
        }

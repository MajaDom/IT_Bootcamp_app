"""Homework Schemas module"""
from typing import Optional
from pydantic import BaseModel, UUID4


class HomeworkSchema(BaseModel):
    """Base schema for Homework"""
    id: UUID4
    link: str
    description: Optional[str]
    due_date: Optional[str]
    file: Optional[bytes]

    class Config:
        """Configuration Class"""
        orm_mode = True


class HomeworkSchemaIn(BaseModel):
    """Base Homework schema for input"""
    link: str
    description: Optional[str]
    due_date: Optional[str]
    file: Optional[bytes]

    class Config:
        """Configuration Class"""
        orm_mode = True
        schema_extra = {
            "example": {
                "link": "Link",
                "description": "Description",
                "due_date": "Due date",
                "file": "File",
            }
        }

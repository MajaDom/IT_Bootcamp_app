"""Lesson Schemas module"""
from typing import Optional
from pydantic import BaseModel, UUID4


class LessonSchema(BaseModel):
    """Base schema for Lesson"""
    id: UUID4
    lesson_title: str
    description: Optional[str]
    content: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True


class LessonSchemaIn(BaseModel):
    """Base Lesson schema for input"""
    lesson_title: str
    description: Optional[str]
    content: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True
        schema_extra = {
            "example": {
                "lesson_title": "Lesson title",
                "description": "Description",
                "content": "Content",
            }
        }

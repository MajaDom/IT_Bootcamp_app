"""Model for Lesson"""
from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Lesson(Base):
    """Base Model for Lesson"""
    __tablename__ = "lessons"
    id = Column(String(100), primary_key=True, default=uuid4)
    lesson_title = Column(String(45), nullable=False)
    description = Column(String(500))
    content = Column(String(1000))

    # TODO: section_id relationship

    def __init__(self, lesson_title: str, description: str, content: str):
        self.lesson_title = lesson_title
        self.description = description
        self.content = content

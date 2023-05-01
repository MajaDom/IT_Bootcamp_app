"""Model for Homework"""
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, BLOB

from app.db import Base


class Homework(Base):
    """Base Model for Homework"""
    __tablename__ = "homeworks"
    id = Column(String(100), primary_key=True, default=uuid4)
    link = Column(String(200))
    description = Column(String(500))
    due_date = Column(DateTime, default=None)
    file = Column(BLOB)

    # TODO: lesson_id relationship

    def __init__(self, link: str, description: str, due_date: str, file):
        self.link = link
        self.description = description
        self.due_date = due_date
        self.file = file

"""Model for Material"""
from uuid import uuid4

from sqlalchemy import Column, String

from app.db import Base


class Material(Base):
    """Base Model for Material"""
    __tablename__ = "materials"
    id = Column(String(100), primary_key=True, default=uuid4)
    material_title = Column(String(100), nullable=False)
    description = Column(String(500))
    content = Column(String(1000))
    file = Column(String(200))

    # TODO: lesson_id relationship

    def __init__(self, material_title: str, description: str, content: str, file: str):
        self.material_title = material_title
        self.description = description
        self.content = content
        self.file = file

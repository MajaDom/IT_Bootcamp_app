"""Projects related models"""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Project(Base):
    """Base model for Project"""
    __tablename__ = "projects"

    id = Column(String(50), primary_key=True, default=uuid4)
    project_title = Column(String(50), nullable=False)
    project_description = Column(String(200))
    due_date = Column(Date())

    # TODO generation_id relationship to be added
    generation_id = Column(String(50), ForeignKey("generation.id"), nullable=False)
    generation = relationship("Generation", lazy="subquery")

    def __init__(self, project_title: str, project_description: str, due_date: str):
        self.project_title = project_title
        self.project_description = project_description
        self.due_date = due_date

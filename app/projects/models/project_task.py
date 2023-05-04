"""Project Task related model"""

from uuid import uuid4
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class Project(Base):
    """Base model for Project Task"""
    __tablename__ = "project_tasks"

    id = Column(String(50), primary_key=True, default=uuid4)
    task_number = Column(Integer, nullable=False)
    task_description = Column(String(200))
    task_max_points = Column(Integer, nullable=False)
    project_id = Column(String(50), ForeignKey("project.id"), nullable=False)
    project = relationship("Project", lazy="subquery")

    # TODO generation_id check if relationship is necessary
    # generation_id = Column(String(50), ForeignKey("generation.id"), nullable=False)
    # generation = relationship("Generation", lazy="subquery")

    def __init__(self, task_number: int, task_description: str, task_max_points: int, project_id: str):
        self.task_number = task_number
        self.task_description = task_description
        self.task_max_points = task_max_points
        self.project_id = project_id

"""Project Task related schemas"""
from typing import Optional

from pydantic import BaseModel, UUID4

from app.projects.schemas import ProjectSchema


class ProjectTaskSchema(BaseModel):
    """Base Project Task schema"""
    id: UUID4
    task_number: int
    task_description: str
    task_max_points: int
    project_id: str
    project: ProjectSchema
    # generation_id: str
    # generation: GenerationSchema
    # TODO generation_id (add if necessary)

    class Config:
        orm_mode = True


class ProjectTaskSchemaIn(BaseModel):
    """Base Project Task schema for input"""
    task_number: int
    task_description: str
    task_max_points: int
    project_id: str
    generation_id: str

    class Config:
        orm_mode = True


class ProjectTaskSchemaUpdate(BaseModel):
    """Base Project schema for update"""
    task_number: Optional[int] = None
    task_description: Optional[str] = None
    task_max_points: Optional[int] = None
    project_id: Optional[str] = None
    generation_id: Optional[str] = None

    class Config:
        orm_mode = True

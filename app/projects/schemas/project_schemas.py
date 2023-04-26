"""Project related schemas"""
from typing import Optional

from pydantic import BaseModel, UUID4

from app.generation.schemas import GenerationSchema


class ProjectSchema(BaseModel):
    """Base Project schema"""
    id: UUID4
    project_title: str
    project_description: str
    due_date: str
    # TODO generation_id (check parameters)
    generation_id: str
    generation: GenerationSchema

    class Config:
        orm_mode = True


class ProjectSchemaIn(BaseModel):
    """Base Project schema for input"""
    project_title: str
    project_description: str
    due_date: str
    generation_id: str

    class Config:
        orm_mode = True


class ProjectSchemaUpdate(BaseModel):
    """Base Project schema for update"""
    project_title: Optional[str] = None
    project_description: Optional[str] = None
    due_date: Optional[str] = None
    generation_id: Optional[str] = None

    class Config:
        orm_mode = True

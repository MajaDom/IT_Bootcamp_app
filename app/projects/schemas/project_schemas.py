"""Project related schemas"""
from typing import Optional

from pydantic import BaseModel, UUID4


class ProjectSchema(BaseModel):
    """Base Project schema"""
    id: UUID4
    project_title: str
    project_description: str
    due_date: str

    # TODO generation_id (check parameters)
    # generation_id: str
    # generation: GenerationSchema

    class Config:
        orm_mode = True

    class ProjectSchemaIn(BaseModel):
        """Base Project schema for input"""
        project_title: str
        project_description: str
        due_date: str

        class Config:
            orm_mode = True

    class ProjectSchemaUpdate(BaseModel):
        """Base Project schema for input"""
        project_title: Optional[str]
        project_description: Optional[str]
        due_date: Optional[str]

        class Config:
            orm_mode = True

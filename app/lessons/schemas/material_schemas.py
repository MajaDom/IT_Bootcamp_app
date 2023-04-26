"""Material Schemas module"""
from typing import Optional
from pydantic import BaseModel, UUID4


class MaterialSchema(BaseModel):
    """Base schema for Material"""
    id: UUID4
    material_title: str
    description: Optional[str]
    content: Optional[str]
    file: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True


class MaterialSchemaIn(BaseModel):
    """Base Material schema for input"""
    material_title: str
    description: Optional[str]
    content: Optional[str]
    file: Optional[str]

    class Config:
        """Configuration Class"""
        orm_mode = True
        schema_extra = {
            "example": {
                "material_title": "Material title",
                "description": "Description",
                "content": "Content",
                "file": "File",
            }
        }

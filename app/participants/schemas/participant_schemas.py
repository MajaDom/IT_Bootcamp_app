from pydantic import BaseModel
from typing import Optional


class ParticipantSchema(BaseModel):
    id: int
    description: Optional[str]
    user_id: str
    consultation_id: int

    class Config:
        orm_mode = True


class ParticipantSchemaIN(BaseModel):
    description: Optional[str]
    consultation_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "description": "I need help with homework."
            }
        }


class ParticipantSchemaUpdate(BaseModel):
    description: Optional[str]
    consultation_id: Optional[int]
    schema_extra = {
        "example": {
            "description": "I need help with homework.",
            "consultation_id": "1"
        }
    }

    class Config:
        orm_mode = True






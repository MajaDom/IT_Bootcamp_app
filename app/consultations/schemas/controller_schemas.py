from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional


class ConsultationSchema(BaseModel):
    id: int
    topic: str
    description: str
    user_id: str
    date_inquired: datetime
    date_confirmed: Optional[datetime]
    date_scheduled: Optional[datetime]
    status: bool
    is_active: bool
    confirmed_by: Optional[str]

    class Config:
        orm_mode = True


class ConsultationSchemaIN(BaseModel):
    topic: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "topic": "Algorithms",
                "description": "Help with binary search"
            }
        }


class ConsultationSchemaUpdate(BaseModel):
    topic: Optional[str]
    description: Optional[str]
    date_scheduled: Optional[str]
    status: bool
    schema_extra = {
        "example": {
            "topic": "Algorithms",
            "description": "Help with binary search",
            "date_scheduled": "2023-10-10 14:00:00",
            "status": "true"
        }
    }

    class Config:
        orm_mode = True






from datetime import date
from pydantic import BaseModel
from pydantic import UUID4
from datetime import date
from app.users.schemas import UserSchema
from app.generation.schemas import GenerationSchema
from typing import Optional

class UserGenerationSchema(BaseModel):
    id: UUID4
    activated_date: date
    deactivated_date: Optional[date]
    is_active: bool
    description: str
    user_id: str
    user: UserSchema
    generation_id: str
    generation: GenerationSchema

    class Config:
        orm_mode = True


class UserGenerationSchemaIn(BaseModel):
    activated_date: str
    deactivated_date: str
    is_active: bool
    description: str
    user_id: str
    generation_id: str
    
    class Config:
        orm_mode = True

class UpdateUserGenerationSchemaIn(BaseModel):
    activated_date: date | None = None
    deactivated_date: date | None = None
    is_active: bool | None = None
    description: str | None = None
    user_id: str | None = None
    generation_id: str | None = None
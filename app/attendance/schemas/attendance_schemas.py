from pydantic import BaseModel
from pydantic import UUID4
from app.user_generation.schemas import UserGenerationSchema
from app.lessons.schemas import LessonSchema

class AttendanceSchema(BaseModel):
    id: UUID4
    description: str
    status: str
    user_generation_id: str
    user_generation: UserGenerationSchema
    lessons_id: str
    lessons: LessonSchema

    class Config:
        orm_mode = True


class AttendanceSchemaIn(BaseModel):
    description: str
    status: str
    user_generation_id: str
    lessons_id: str
    
    class Config:
        orm_mode = True

class UpdateAttendanceSchemaIn(BaseModel):
    description: str | None = None
    status: str | None = None
    user_generation_id: str | None = None
    lessons_id: str | None = None

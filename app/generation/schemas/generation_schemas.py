from datetime import date, datetime
import datetime
from pydantic import BaseModel
from pydantic import UUID4
from datetime import date
from app.course.schemas import CourseSchema

class GenerationSchema(BaseModel):
    id: UUID4
    name: str
    start_date: date
    end_date: date
    is_active: bool
    course_id: str
    course: CourseSchema


    class Config:
        orm_mode = True


class GenerationSchemaIn(BaseModel):
    name: str
    start_date: str
    end_date: str
    is_active: str
    course_id: str
    
    class Config:
        orm_mode = True

class UpdateGenerationSchemaIn(BaseModel):
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    is_active: bool | None = None
    course_id: str | None = None

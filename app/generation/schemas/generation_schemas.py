from datetime import date
from pydantic import BaseModel
from pydantic import UUID4
from datetime import date
from app.course.schemas import CourseSchema

# The class GenerationSchema is a subclass of BaseModel in Python.
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


# The class GenerationSchemaIn is a data model for input parameters used in generating a schema.
class GenerationSchemaIn(BaseModel):
    name: str
    start_date: str
    end_date: str
    is_active: bool
    course_id: str
    
    class Config:
        orm_mode = True

# The class UpdateGenerationSchemaIn is a BaseModel used for updating generation schema.
class UpdateGenerationSchemaIn(BaseModel):
    name: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    is_active: bool | None = None
    course_id: str | None = None

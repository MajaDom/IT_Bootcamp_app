from pydantic import BaseModel
from pydantic import UUID4


class CourseSchema(BaseModel):
    id: UUID4
    course_name: str
    course_description: str

    class Config:
        orm_mode = True


class CourseSchemaIn(BaseModel):
    course_name: str
    course_description: str

    class Config:
        orm_mode = True
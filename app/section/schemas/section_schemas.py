from datetime import date, datetime
import datetime
from pydantic import BaseModel
from pydantic import UUID4
from datetime import date
from app.generation.schemas import GenerationSchema

class SectionSchema(BaseModel):
    id: UUID4
    section_title: str
    start_date: date
    end_date: date
    generation_id: str
    generation: GenerationSchema


    class Config:
        orm_mode = True


class SectionSchemaIn(BaseModel):
    section_title: str
    start_date: str
    end_date: str
    generation_id: str
    
    class Config:
        orm_mode = True

class UpdateSectionSchemaIn(BaseModel):
    section_title: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    generation_id: str | None = None
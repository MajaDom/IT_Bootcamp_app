from pydantic import BaseModel, UUID4


class ConsultationSchema(BaseModel):
    id: int
    topic: str
    description: str
    user_id: str
    date_inquired: str
    date_confirmed: str
    date_scheduled: str
    status: bool
    is_active: bool

    class Config:
        orm_mode = True


class ConsultationSchemaIN(BaseModel):
    topic: str
    description: str

    class Config:
        orm_mode = True


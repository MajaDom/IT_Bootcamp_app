from pydantic import BaseModel, UUID4


class ConsultationSchema(BaseModel):
    id: int
    topic: str
    description: str
    user_id: str

    class Config:
        orm_mode = True


class ConsultationSchemaIN(BaseModel):
    topic: str
    description: str
    user_id: str

    class Config:
        orm_mode = True


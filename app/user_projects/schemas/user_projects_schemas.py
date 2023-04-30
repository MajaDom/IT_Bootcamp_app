from pydantic import BaseModel
from pydantic import UUID4

class UserProjectsSchema(BaseModel):
    id: UUID4
    name: str
    scope: str
    link: str
    file: bytes
    status: str
    additional: str

    #TO DO after the user generation has been done
    # user_generation_id: str
    # user_generation: UserGenerationSchema


    class Config:
        orm_mode = True


class UserProjectsSchemaIn(BaseModel):
    name: str
    scope: str
    link: str
    file: bytes
    status: str
    additional: str   

    #TO DO after user generation has been done
    # user_generation_id: str
    
    class Config:
        orm_mode = True

class UpdateUserProjectsSchemaIn(BaseModel):
    name: str | None = None
    scope: str | None = None
    link: str | None = None
    file: bytes | None = None
    status: str | None = None
    additional: str | None = None
    #TO TO
    #user_generation_id
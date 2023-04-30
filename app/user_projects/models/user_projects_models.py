from uuid import uuid4
# from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, LargeBinary

from app.db import Base


class UserProjects(Base):
    __tablename__ = "user_projects"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))
    scope = Column(String(100))
    link = Column(String(45))
    file = Column(LargeBinary)
    status = Column(String(45))
    additional = Column(String(500))

    #TO DO when user_generation is done

    # user_generation_id = Column(String(45), ForeignKey("usergeneration.id"))
    # user_generation = relationship("UserGeneration", lazy='subquery')

    def __init__(self, name: str, scope: str, link: str, file: bytes, status: str, additional: str ):
        self.name = name
        self.scope = scope
        self.link = link
        self.file = file
        self.status = status
        self.additional = additional 
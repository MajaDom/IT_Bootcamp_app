from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, String

from app.db import Base


class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    description = Column(String(500))
    status = Column(String(100))

    user_generation_id = Column(String(45), ForeignKey("user_generation.id"))
    user_generation = relationship("UserGeneration", lazy='subquery')

    lessons_id = Column(String(45), ForeignKey("lessons.id"))
    lessons = relationship("Lesson", lazy='subquery')
    

    def __init__(self, description: str, status: str, user_generation_id: str, lessons_id:str ):
        self.description = description
        self.status = status
        self.user_generation_id = user_generation_id
        self.lessons_id = lessons_id
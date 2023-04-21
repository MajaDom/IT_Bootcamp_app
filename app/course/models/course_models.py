from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4

class Course(Base):
    __tablename__ = "course"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    course_name = Column(String(200), unique=True)
    course_description = Column(String(500))

    def __init__(self, course_name, course_description):
        self.course_name = course_name
        self.course_description = course_description
from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, UniqueConstraint, CheckConstraint

from app.db import Base


class Generation(Base):
    __tablename__ = "generation"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))  # i.e. '2021/2022'
    start_date = Column(Date)
    end_date = Column(Date)
    is_active = Column(Boolean)
    __table_args__ = (UniqueConstraint("name", "start_date", "end_date", name="name_start_date_end_date_uc"),
                      CheckConstraint(start_date < end_date, name='check_start_date_end_date'))

    course_id = Column(String(45), ForeignKey("course.id"))
    course = relationship("Course", lazy='subquery')

    def __init__(self, name: str, start_date: str, end_date: str, is_active: bool, course_id ):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.is_active = is_active
        self.course_id = course_id

        
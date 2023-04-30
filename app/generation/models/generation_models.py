from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, UniqueConstraint, CheckConstraint

from app.db import Base


# The class "Generation" is a subclass of "Base".
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
        """
        This is a constructor function that initializes the attributes of a class object with the given
        parameters.
        
        :param name: A string representing the name of a course
        :type name: str
        :param start_date: The start date of a course, represented as a string in the format
        "YYYY-MM-DD"
        :type start_date: str
        :param end_date: The "end_date" parameter is a string that represents the end date of a course.
        It is converted to a datetime object using the "datetime.strptime()" method in the constructor
        :type end_date: str
        :param is_active: is_active is a boolean parameter that indicates whether the course is
        currently active or not. If the value is True, it means the course is active, and if the value
        is False, it means the course is inactive
        :type is_active: bool
        :param course_id: The `course_id` parameter is a variable that represents the unique identifier
        of a course. It is likely used to associate the course with other objects or data structures in
        the program
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.is_active = is_active
        self.course_id = course_id
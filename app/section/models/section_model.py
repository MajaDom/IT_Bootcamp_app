from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, UniqueConstraint, CheckConstraint

from app.db import Base


class Section(Base):
    __tablename__ = "section"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    section_title = Column(String(100))  # i.e. '2021/2022'
    start_date = Column(Date)
    end_date = Column(Date)
    __table_args__ = (UniqueConstraint("section_title", "start_date", "end_date", section_title="section_title_start_date_end_date_uc"),
                      CheckConstraint(start_date < end_date, section_title='check_start_date_end_date'))

    generation_id = Column(String(45), ForeignKey("generation.id"))
    generation = relationship("Generation", lazy='subquery')

    def __init__(self, section_title: str, start_date: str, end_date: str, generation_id):
        self.section_title = section_title
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.generation_id = generation_id
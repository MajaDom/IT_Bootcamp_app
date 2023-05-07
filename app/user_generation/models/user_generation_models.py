from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, Date, ForeignKey, String, UniqueConstraint, CheckConstraint

from app.db import Base


class UserGeneration(Base):
    __tablename__ = "user_generation"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    activated_date = Column(Date)
    deactivated_date = Column(Date, default=None)
    is_active = Column(Boolean, default=True)
    description = Column(String(100))

    # __table_args__ = (UniqueConstraint("activated_date", "deactivated_date", "is_active", "description", description="description_activated_date_deactivated_date_uc"),
    #                   CheckConstraint(activated_date < deactivated_date, description='check_activated_date_deactivated_date'))

    user_id = Column(String(45), ForeignKey("users.id"))
    user = relationship("User", lazy='subquery')

    generation_id = Column(String(45), ForeignKey("generation.id"))
    generation = relationship("Generation", lazy='subquery')    

    def __init__(self, activated_date: str, deactivated_date: str, is_active: bool, description: str, user_id: str, generation_id:str ):
        self.activated_date = datetime.strptime(activated_date, "%Y-%m-%d")
        self.deactivated_date = datetime.strptime(deactivated_date, "%Y-%m-%d")
        self.is_active = is_active
        self.description = description
        self.user_id = user_id
        self.generation_id = generation_id
       

"""Model for Consultation"""

from app.db.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Consultation(Base):
    """Model for Consultation"""
    __tablename__ = "consultations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(200), nullable=False)  # topic that is going to be covered
    description = Column(String(500), nullable=True)  # more details about the problem that requires consultation
    date_inquired = Column(DateTime, default=datetime.now())  # automatically filled based on the date of inquiry
    date_confirmed = Column(DateTime, default=None)  # automatically filled when the status changes
    date_scheduled = Column(DateTime, default=None)  # date of the consultation
    status = Column(Boolean, default=False)  # consultation confirmation

    is_active = Column(Boolean, default=True)  # when the schedule date has passed, is_active is automatically False

    confirmed_by = Column(String(40), ForeignKey("users.id"), default=None)
    user_id = Column(String(40), ForeignKey("users.id"), nullable=False)
    # user = relationship("User", back_populates="consultation") # TODO add relationship User

    def __init__(self, topic: str, description: str, user_id: str):
        self.topic = topic
        self.description = description
        self.user_id = user_id



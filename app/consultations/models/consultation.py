"""Model for Consultation"""

from app.db.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Consultation(Base):
    __tablename__ = "consultations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    topic = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    date_inquired = Column(DateTime, default=datetime.now())
    date_confirmed = Column(DateTime, default=None)
    date_scheduled = Column(DateTime, default=None)
    status = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    user_id = Column(String(40), ForeignKey("users.id"), nullable=False)
    # user = relationship("User", back_populates="consultation") # TODO add relationship User

    def __init__(self, topic: str, description: str, user_id: str):
        self.topic = topic
        self.description = description
        self.user_id = user_id



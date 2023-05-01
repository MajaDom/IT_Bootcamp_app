"""Model for Participant"""

from app.db.database import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class Participant(Base):
    """Model for Participant"""
    __tablename__ = "participants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(500), nullable=True)  # more details about the problem that requires consultation

    user_id = Column(String(40), ForeignKey("users.id"), nullable=False)
    consultation_id = Column(Integer, ForeignKey("consultations.id"), nullable=False)
    participant = relationship("Consultation", back_populates="consultation")

    def __init__(self, description: str, user_id: str, consultation_id: int):
        self.description = description
        self.user_id = user_id
        self.consultation_id = consultation_id



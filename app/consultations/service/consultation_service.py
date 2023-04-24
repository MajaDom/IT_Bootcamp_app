from app.consultations.repository import ConsultationRepository
from app.db.database import SessionLocal
from app.consultations.models import Consultation


class ConsultationService:
    """Service for Consultations routes."""
    @staticmethod
    def create_new_consultation(topic: str, description: str, user_id: str):
        try:
            with SessionLocal() as db:
                repository = ConsultationRepository(db, Consultation)
                fields = {"topic": topic, "description": description, "user_id": user_id}
                consultation = repository.create(fields)
            return consultation
        except Exception as exc:
            raise exc

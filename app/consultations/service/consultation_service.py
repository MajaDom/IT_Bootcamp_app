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

    @staticmethod
    def read_all_consultations():
        try:
            with SessionLocal() as db:
                repository = ConsultationRepository(db, Consultation)
                consultations = repository.read_all()
            return consultations
        except Exception as exc:
            raise exc

    @staticmethod
    def read_consultation(consultation_id: int):
        try:
            with SessionLocal() as db:
                repository = ConsultationRepository(db, Consultation)
                consultations = repository.read_by_id(model_id=consultation_id)
            return consultations
        except Exception as exc:
            raise exc

    @staticmethod
    def update_consultation(consultation_id: int, updates: dict):
        try:
            with SessionLocal() as db:
                repository = ConsultationRepository(db, Consultation)
                db_obj = repository.read_by_id(model_id=consultation_id)
                consultation = repository.update(db_obj=db_obj, updates=updates)
            return consultation
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_consultation(consultation_id: int):
        try:
            with SessionLocal() as db:
                repository = ConsultationRepository(db, Consultation)
                return repository.delete(model_id=consultation_id)
        except Exception as exc:
            raise exc




                



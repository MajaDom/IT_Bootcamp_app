from app.participants.repository import ParticipantRepository
from app.db.database import SessionLocal
from app.participants.models import Participant


class ParticipantService:
    """Service for Participant routes."""

    @staticmethod
    def create_new_participant(description: str, consultation_id: int, user_id:str):
        try:
            with SessionLocal() as db:
                repository = ParticipantRepository(db, Participant)
                fields = {"description": description, "consultation_id": consultation_id, "user_id": user_id}
                participant = repository.create(fields)
            return participant
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all_participants():
        try:
            with SessionLocal() as db:
                repository = ParticipantRepository(db, Participant)
                participants = repository.read_all()
            return participants
        except Exception as exc:
            raise exc

    @staticmethod
    def read_participants_of_one_consultation(consultation_id: int):
        try:
            with SessionLocal() as db:
                repository = ParticipantRepository(db, Participant)
                participants = repository.read_participants_by_consultation_id(consultation_id=consultation_id)
            return participants
        except Exception as exc:
            raise exc

    @staticmethod
    def update_participant(participant_id: int, updates: dict):
        try:
            with SessionLocal() as db:
                repository = ParticipantRepository(db, Participant)
                db_obj = repository.read_by_id(model_id=participant_id)
                participant = repository.update(db_obj=db_obj, updates=updates)
            return participant
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_participant(participant_id: int):
        try:
            with SessionLocal() as db:
                repository = ParticipantRepository(db, Participant)
                return repository.delete(model_id=participant_id)
        except Exception as exc:
            raise exc








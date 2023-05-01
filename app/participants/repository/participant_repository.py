"""Repository for Participant"""

from sqlalchemy.exc import IntegrityError
from typing import Union
from app.participants.models import Participant

from app.base import BaseCRUDRepository, AppException


class ParticipantRepository(BaseCRUDRepository):
    """Repository for Participant Model"""

    def create(self, attributes: dict) -> Participant:
        """
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_all(self) -> list[Participant]:
        """
        Read all function returns all participants from the database.
        """
        try:
            return super().read_all()
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_by_id(self, model_id: Union[str, int]) -> Participant:
        """
        Function read_by_id returns one participant from the database based on provided id.
        """
        try:
            return super().read_by_id(model_id)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_participants_by_consultation_id(self, consultation_id: int) -> list[Participant]:
        """

        """
        try:
            participants = self.db.query(Participant).filter(Participant.consultation_id == consultation_id).all()
            return participants
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def update(self, db_obj, updates: dict) -> Participant:
        """
        Function update updates desired participant
        """
        try:
            return super().update(db_obj, updates)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def delete(self, model_id: Union[str, int]):
        try:
            return super().delete(model_id)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

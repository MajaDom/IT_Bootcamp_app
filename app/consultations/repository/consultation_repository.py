"""Repository for Consultation"""

from sqlalchemy.exc import IntegrityError
from typing import Union
from app.consultations.models import Consultation

from app.base import BaseCRUDRepository, AppException


class ConsultationRepository(BaseCRUDRepository):
    """Repository for Consultation Model"""

    def create(self, attributes: dict) -> Consultation:
        """
        The create function creates a new consultation in the database.
        It takes an attributes dictionary as its only parameter, and returns the created Consultation object.

        Param attributes:dict: Pass in the attributes that are being passed into the create function.
        Return: The created object.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_all(self) -> list[Consultation]:
        """
        Read all function returns all consultations from the database.
        """
        try:
            consultations = self.db.query(Consultation).all()
            return consultations
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_by_id(self, model_id: Union[str, int]) -> Consultation:
        """
        Function read_by_id returns one consultation from the database based on provided id.
        """
        try:
            return super().read_by_id(model_id)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def update(self, db_obj, updates: dict) -> Consultation:
        """
        Function update updates desired consultation
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

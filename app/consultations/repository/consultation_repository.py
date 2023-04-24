"""Repository for Consultation"""

from sqlalchemy.exc import IntegrityError

from app.base import BaseCRUDRepository, AppException


class ConsultationRepository(BaseCRUDRepository):
    """Repository for Consultation Model"""

    def create(self, attributes: dict):
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

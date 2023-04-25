"""Lesson Repository module"""
from sqlalchemy.exc import IntegrityError
from app.base import BaseCRUDRepository, AppException


class LessonRepository(BaseCRUDRepository):
    """Repository for Lesson Model"""
    def create(self, attributes: dict):
        """
        The create function creates a new lesson in the database.
        It takes an attributes dictionary as its only parameter, and returns the created Lesson object.

        Param attributes:dict: Pass in the attributes that are being passed into the create function.
        Return: The created object.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_all(self):
        """
        Function is used to retrieve all the objects from a table.
        It takes no arguments and returns a list of model objects.

        Return: All the models of a specific model.
        """
        try:
            return super().read_all()
        except Exception as exc:
            self.db.rollback()
            raise AppException(message=str(exc), code=500) from exc

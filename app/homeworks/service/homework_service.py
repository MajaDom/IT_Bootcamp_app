"""Homework Service module"""


from app.homeworks.exceptions.homework_exceptions import HomeworkDoesNotExistsException
from app.homeworks.repositories import HomeworkRepository
from app.db.database import SessionLocal
from app.homeworks.models import Homework


class HomeworkService:
    """Service for Homework routes."""

    @staticmethod
    def create_new_homework(link: str, description: str, due_date: str, file):
        """
        The create_new_homework function creates a new homework in the database.
        It takes as input a link, description, due_date and file.
        The function returns the newly created homework.

        Param link:str: Store the link.
        Param description:str: Description.
        Param due_date:str: Due date.
        Param file:str: File.
        Return: The homework object that was created.
        """
        try:
            with SessionLocal() as db:
                repository = HomeworkRepository(db, Homework)
                fields = {
                    "link": link,
                    "description": description,
                    "due_date": due_date,
                    "file": file,
                }
                obj = repository.create(fields)
            return obj
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                repository = HomeworkRepository(db, Homework)
                objs = repository.read_all()
                if not objs:
                    raise HomeworkDoesNotExistsException(message=f"No homeworks in our Database.")
            return repository.read_all()
        except Exception as exc:
            raise exc

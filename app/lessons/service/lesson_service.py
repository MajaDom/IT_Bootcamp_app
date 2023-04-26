"""Lesson Service module"""


from app.lessons.exceptions.lesson_exceptions import LessonDoesNotExistsException
from app.lessons.repositories import LessonRepository
from app.db.database import SessionLocal
from app.lessons.models import Lesson


class LessonService:
    """Service for Lesson routes."""

    @staticmethod
    def create_new_lesson(lesson_title: str, description: str, content: str):
        """
        The create_new_lesson function creates a new lesson in the database.
        It takes as input a lesson_title, description, and content code.
        The function returns the newly created lesson.

        Param lesson_title:str: Store the lesson title.
        Param password:str: Hash the password.
        Param description:str: Description.
        Param content:str: Content.
        Return: The lesson object that was created.
        """
        try:
            with SessionLocal() as db:
                repository = LessonRepository(db, Lesson)
                fields = {
                    "lesson_title": lesson_title,
                    "description": description,
                    "content": content,
                }
                obj = repository.create(fields)
            return obj
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                repository = LessonRepository(db, Lesson)
                objs = repository.read_all()
                if not objs:
                    raise LessonDoesNotExistsException(message=f"No lessons in our Database.")
            return repository.read_all()
        except Exception as exc:
            raise exc

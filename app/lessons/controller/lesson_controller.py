"""Lesson Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.lessons.service import LessonService


class LessonController:
    """Controller for Lesson routes"""
    @staticmethod
    def create_lesson(lesson_title: str, description: str, content: str):
        """
        Function creates a new lesson in the database.
        It takes as input a lesson_title, description and content. It returns a response with
        status code 200 if the creation was successful, or 400 if not.

        Param lesson_title: Receive the lesson title
        Param description: Store the description of the lesson
        Param content: Store the content of the lesson.
        Return: A response object.
        """
        try:
            return LessonService.create_new_lesson(lesson_title, description, content)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_all():
        try:
            return LessonService.read_all()
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

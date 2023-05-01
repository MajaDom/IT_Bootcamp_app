"""Homework Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.homeworks.service import HomeworkService


class HomeworkController:
    """Controller for Homework routes"""
    @staticmethod
    def create_homework(link: str, description: str, due_date: str, file):
        """
        Function creates a new homework in the database.
        It takes as input a link, description, due_date and file. It returns a response with
        status code 200 if the creation was successful, or 400 if not.

        Param link: Receive the link
        Param description: Store the description of the homework
        Param due_date: Store the due date of the homework.
        Return: A response object.
        """
        try:
            return HomeworkService.create_new_homework(link, description, due_date, file)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_all():
        try:
            return HomeworkService.read_all()
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

"""Project Task Repository module"""
from sqlalchemy.exc import IntegrityError

from app.base import BaseCRUDRepository, AppException
from app.projects.exceptions.project_task_exceptions import ProjectTaskNotFoundException
from app.projects.models import ProjectTask


class ProjectRepository(BaseCRUDRepository):
    """Repository for Project Task Model"""

    def create(self, attributes: dict):
        """
        The create function creates a new project task in the database.
        It takes an attributes dictionary as its only parameter, and returns the created ProjectTask object.

        Param attributes:dict: Pass in the attributes that are being passed into the create function.
        Return: The created object.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_project_task_by_min_points(self, min_points: str):
        """
        Function takes a part of project title as an argument and returns the project task object.
        If no such project task exists, it raises an exception.

        Param part_of_project_title: str: Find project tasks that have more or equal than provided min points.
        Return: A project task object if exists.
        """
        try:
            project_task = self.db.query(ProjectTask).filter(ProjectTask.task_max_points >= min_points).limit(20).all()
            if not project_task:
                self.db.rollback()
                raise ProjectTaskNotFoundException(message=f"Project task with more than {min_points} not found",
                                                   code=404)
            return project_task
        except Exception as exc:
            self.db.rollback()
            raise exc

    def read_project_task_by_task_number(self, task_number: int):
        """
        Function takes task number as an argument and returns the project task object.
        If no such project task exists, it raises an exception.

        Param task_number: int: Find project task with that task number.
        Return: A project task object if exists.
        """
        try:
            project_task = self.db.query(ProjectTask).filter(ProjectTask.task_number == task_number).first()
            if not project_task:
                self.db.rollback()
                raise ProjectTaskNotFoundException(
                    message=f"Project task with provided task number:  {task_number}, not found", code=404)
            return project_task
        except Exception as exc:
            self.db.rollback()
            raise exc

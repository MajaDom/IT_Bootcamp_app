"""Project Repository module"""
from sqlalchemy.exc import IntegrityError

from app.base import BaseCRUDRepository, AppException
from app.projects.exceptions import ProjectNotFoundException
from app.projects.models import Project


class ProjectRepository(BaseCRUDRepository):
    """Repository for Project Model"""
    def create(self, attributes: dict):
        """
        The create function creates a new project in the database.
        It takes an attributes dictionary as its only parameter, and returns the created Project object.

        Param attributes:dict: Pass in the attributes that are being passed into the create function.
        Return: The created object.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Something went wrong.", code=400) from exc

    def read_project_by_part_of_title(self, part_of_project_title: str):
        """
        Function takes a part of project title as an argument and returns the project object.
        If no such project exists, it raises an exception.

        Param part_of_project_title: str: Find projects that have those part of title.
        Return: A project object if exists.
        """
        try:
            project = self.db.query(Project).filter(Project.project_title.ilike(f"%{part_of_project_title}%")).limit(20).all()
            if not project:
                self.db.rollback()
                raise ProjectNotFoundException
            return project
        except Exception as exc:
            self.db.rollback()
            raise exc

"""Project Service module"""
from app.db import SessionLocal
from app.projects.models import Project
from app.projects.repository import ProjectRepository


class ProjectService:
    """Service for Project routes."""

    @staticmethod
    def create_new_project(project_title: str, project_description: str, due_date: str, generation_id: str):
        """
        Creates a new project in the database with the given project title, project description, due date,
        and generation ID.

        Param project_title: str: The title of the project.
        Param project_description: str: The description of the project.
        Param due_date: str: The due date of the project.
        Param generation_id: str: ID of student generation

        Returns: The created project object.

        Raises: Exception: If there is an error creating the project.
        """
        try:
            with SessionLocal() as db:
                project_repository = ProjectRepository(db, Project)
                fields = {"project_title": project_title, "project_description": project_description,
                          "due_date": due_date, "generation_id": generation_id}
                project_obj = project_repository.create(fields)
                return project_obj
        except Exception as exc:
            raise exc

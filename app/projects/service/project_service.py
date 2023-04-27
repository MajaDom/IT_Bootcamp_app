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

    @staticmethod
    def read_all_projects():
        """
        Reads all projects from the database.

        Returns: List[Project]: A list of Project objects.

        Raises: Exception: If an error occurs while reading projects from the database.
        """
        try:
            with SessionLocal() as db:
                project_repository = ProjectRepository(db, Project)
            return project_repository.read_all()
        except Exception as exc:
            raise exc

    @staticmethod
    def read_project_by_id(project_id: str):
        """
        Reads a project from the database by its ID.

        Param project_id: str: The ID of the project to read.

        Returns: Project: The project with the specified ID.

        Raises: Exception: If an error occurs while reading the project from the database.
        """
        try:
            with SessionLocal() as db:
                project_repository = ProjectRepository(db, Project)
            return project_repository.read_by_id(project_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def read_project_by_title(project_title: str):
        """
        Reads a project from the database by its title or part of title.

        Param project_title: str: The title or part of title of the project to read.

        Returns: Project: The project with the provided title if exists.

        Raises: Exception: If an error occurs while reading the project from the database.
        """
        try:
            with SessionLocal() as db:
                project_repository = ProjectRepository(db, Project)
            return project_repository.read_project_by_part_of_title(project_title)
        except Exception as exc:
            raise exc

    @staticmethod
    def update_project_by_id(project_id: str, project):
        """
        Update a project data from the database by provided project_id.

        Param project_id: str: The ID of the project to update.

        Returns: Project: The project with the provided title if exists.

        Raises: Exception: If an error occurs while reading the project from the database.
        """
        try:
            with SessionLocal() as db:
                project_repository = ProjectRepository(db, Project)
                project_obj = project_repository.read_by_id(project_id)
            return project_repository.update(project_obj, project)
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_project_by_id(project_id: str):
        try:
            with SessionLocal() as db:
            project_repository = ProjectRepository(db, Project)
            return project_repository.delete(project_id)
        except Exception as exc:
            raise exc

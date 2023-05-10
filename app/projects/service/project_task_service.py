"""Project Task Service module"""
from app.db import SessionLocal
from app.projects.models import ProjectTask
from app.projects.repository import ProjectTaskRepository


class ProjectTaskService:
    """Service for Project Task routes."""

    @staticmethod
    def create_new_project_task(task_number: int, task_description: str, task_max_points: int, project_id: str):
        """
        Creates a new project task in the database with the given task number, task description, task max points,
        and project ID.

        Param task_number: int: The project task number.
        Param task_description: str: The description of the project task.
        Param task_max_points: int: The maximum number of points that could be achieved.
        Param project_id: str: ID of project

        Returns: The created project task object.

        Raises: Exception: If there is an error creating the project task.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
                fields = {"task_number": task_number, "task_description": task_description,
                          "task_max_points": task_max_points, "project_id": project_id}
                project_task_obj = project_task_repository.create(fields)
                return project_task_obj
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all_project_tasks():
        """
        Reads all project tasks from the database.

        Returns: List[ProjectTask]: A list of Project Task objects.

        Raises: Exception: If an error occurs while reading project tasks from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
            return project_task_repository.read_all().limit(30)
        except Exception as exc:
            raise exc

    @staticmethod
    def read_project_task_by_id(project_task_id: str):
        """
        Reads a project task from the database by its ID.

        Param project_task_id: str: The ID of the project task to read.

        Returns: ProjectTask: The project task with the specified ID.

        Raises: Exception: If an error occurs while reading the project from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
            return project_task_repository.read_by_id(project_task_id)
        except Exception as exc:
            raise exc

    @staticmethod
    def read_project_task_by_number(task_number: int):
        """
        Reads a project task from the database by task_number.

        Param task_number: int: The number of the project task to read.

        Returns: ProjectTask: The project task with the specified task number.

        Raises: Exception: If an error occurs while reading the project task from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
            return project_task_repository.read_project_task_by_task_number(task_number)
        except Exception as exc:
            raise exc

    @staticmethod
    def read_project_task_by_min_points(min_points: int):
        """
        Reads a project task from the database that have more than provided minimum points.

        Param min_points: int: Minimum points.

        Returns: ProjectTask: The project task with more points than the provided, if exists.

        Raises: Exception: If an error occurs while reading the project task from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
            return project_task_repository.read_project_task_by_min_points(min_points)
        except Exception as exc:
            raise exc

    @staticmethod
    def update_project_task_by_id(project_task_id: str, project_task: dict):
        """
        Update a project task data from the database by provided project_task_id.

        Param project_task_id: str: The ID of the project task to update.

        Returns: ProjectTask: The project task with the provided ID, if exists.

        Raises: Exception: If an error occurs while reading the project task from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
                project_task_obj = project_task_repository.read_by_id(project_task_id)
            return project_task_repository.update(project_task_obj, project_task)
        except Exception as exc:
            raise exc

    @staticmethod
    def delete_project_task_by_id(project_task_id: str):
        """
        Delete a project task from the database by provided project_task_id.

        Param project_task_id: str: The ID of the project task to delete.

        Raises: Exception: If an error occurs while reading the project task from the database.
        """
        try:
            with SessionLocal() as db:
                project_task_repository = ProjectTaskRepository(db, ProjectTask)
                return project_task_repository.delete(project_task_id)
        except Exception as exc:
            raise exc

"""Project Controller module"""
from fastapi import HTTPException

from app.base import AppException
from app.projects.service import ProjectService


class ProjectController:
    """Controller for Project routes."""

    @staticmethod
    def create_new_project(project_title: str, project_description: str, due_date: str, generation_id: str):
        """
        Creates a new project with the given title, description, due date, and generation ID.

            Param project_title: str: The title of the project.
            Param project_description: str: The description of the project.
            Param due_date: str: The due date of the project.
            Param generation_id: str: ID of student generation

            Returns: dict: A dictionary containing the details of the newly created project.

            Raises: HTTPException: If there is an error while creating the project. The status code and detail
            message depend on the error.
        """

        try:
            return ProjectService.create_new_project(project_title, project_description, due_date, generation_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

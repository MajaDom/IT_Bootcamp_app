"""Project Controller module"""
from fastapi import HTTPException, Response

from app.base import AppException
from app.projects.exceptions import ProjectNotFoundException
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

    @staticmethod
    def get_all_projects():
        """
        Retrieve all projects from the database.

        Returns: list: A list of Project objects representing all projects.

        Raises: HTTPException: If there is an application-specific error or a server-side error.
        The status code and detail message depend on the error.

        """
        try:
            projects = ProjectService.read_all_projects()
            return projects
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_project_by_id(project_id: str):
        """
        Fetches a single project by its ID.

        Param: project_id: str: The unique ID of the project to retrieve.

        Returns: Project: An instance of the Project model representing the project with the specified ID.

        Raises: HTTPException: If the specified project ID is invalid or the operation failed for any other reason.
        """
        try:
            project = ProjectService.read_project_by_id(project_id)
            return project
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_project_by_title(project_title: str):
        """
        Read a project by its title.

        Param: project_id: str: The title or part of title of the project.

        Returns: Project: Project object if found.

        Raises: HTTPException: If an error occurs while processing the request.
        """
        try:
            project = ProjectService.read_project_by_title(project_title)
            if project:
                return project
            return Response(content=f"Project with title does not exist")
        except ProjectNotFoundException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def update_project_by_id(project_id: str, project: dict):
        """
        Updates a project with the specified ID using the data in the given dictionary.

        Params: project_id: str: The ID of the project to update.
                project: dict: A dictionary containing the fields to update.

        Returns: dict: A dictionary representing the updated project.

        Raises: HTTPException: If an error occurs while updating the project.
        """
        try:
            project = ProjectService.update_project_by_id(project_id, project)
            return project
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def delete_project_by_id(project_id: str):
        try:
            ProjectService.delete_project_by_id(project_id)
            return Response(content=f"Project with id: {project_id} is deleted")
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

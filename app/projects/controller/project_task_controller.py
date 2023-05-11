"""Project Task Controller module"""
from fastapi import HTTPException, Response

from app.base import AppException
from app.projects.service import ProjectTaskService


class ProjectTaskController:
    """Controller for Project Task routes."""

    @staticmethod
    def create_new_project_task(task_number: int, task_description: str, task_max_points: int, project_id: str):
        """
        Creates a new project task with the given task number, description, maximum points and project ID.

            Param task_number: int: The project task number.
            Param task_description: str: The description of the project task.
            Param task_max_points: int: The maximum number of points that could be achieved.
            Param project_id: str: ID of project

            Returns: dict: A dictionary containing the details of the newly created project task.

            Raises: HTTPException: If there is an error while creating the project task. The status code and detail
            message depend on the error.
        """

        try:
            return ProjectTaskService.create_new_project_task(task_number, task_description, task_max_points,
                                                              project_id)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message)
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_all_project_tasks():
        """
        Retrieve all project tasks from the database.

        Returns: list: A list of ProjectTask objects representing all project tasks.

        Raises: HTTPException: If there is an application-specific error or a server-side error.
        The status code and detail message depend on the error.

        """
        try:
            project_tasks = ProjectTaskService.read_all_project_tasks()
            return project_tasks
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_project_task_by_id(project_task_id: str):
        """
        Fetches a single project task by its ID.

        Param: project_task_id: str: The unique ID of the project task to retrieve.

        Returns: ProjectTask: An instance of the ProjectTask model representing the project task with the specified ID.

        Raises: HTTPException: If the specified project task ID is invalid or the operation failed for any other reason.
        """
        try:
            project_task = ProjectTaskService.read_project_task_by_id(project_task_id)
            return project_task
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_project_task_by_number(task_number: int):
        """
        Read a project task by its number.

        Param: task_number: int: The number of the project task.

        Returns: ProjectTask: An instance of the ProjectTask model representing the project task with
                              the specified task number.

        Raises: HTTPException: If an error occurs while processing the request.
        """
        try:
            project_task = ProjectTaskService.read_project_task_by_number(task_number)
            if project_task:
                return project_task
            return Response(content=f"Project task with provided number: {task_number}, does not exist")
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def get_project_task_by_min_points(min_points: int):
        """
        Read project tasks that have more than provided minimum points.

        Param: min_points: int: The minimum number of the points.

        Returns: ProjectTask: Project task object if found.

        Raises: HTTPException: If an error occurs while processing the request.
        """
        try:
            project_tasks = ProjectTaskService.read_project_task_by_min_points(min_points)
            if project_tasks:
                return project_tasks
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def update_project_task_by_id(project_task_id: str, project_task: dict):
        """
        Updates a project task with the specified ID using the data in the given dictionary.

        Params: project_task_id: str: The ID of the project task to update.
                project_task: dict: A dictionary containing the fields to update.

        Returns: dict: A dictionary representing the updated project task.

        Raises: HTTPException: If an error occurs while updating the project task.
        """
        try:
            project_task = ProjectTaskService.update_project_task_by_id(project_task_id, project_task)
            return project_task
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def delete_project_task_by_id(project_task_id: str):
        try:
            ProjectTaskService.delete_project_task_by_id(project_task_id)
            return Response(content=f"Project task with id: {project_task_id} is deleted")
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

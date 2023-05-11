from fastapi import APIRouter

from app.projects.controller import ProjectController
from app.projects.controller.project_task_controller import ProjectTaskController
from app.projects.schemas import ProjectSchema, ProjectSchemaIn, ProjectSchemaUpdate, ProjectTaskSchema, \
    ProjectTaskSchemaIn, ProjectTaskSchemaUpdate

# Project Router starts here
project_router = APIRouter(prefix="/api/projects", tags=["Projects"])


@project_router.post("/add-new-project", response_model=ProjectSchema)
def create_new_project(project: ProjectSchemaIn):
    """
    Create a new project with the specified project details.

    Args: project (ProjectSchemaIn): The project details.

    Returns: ProjectSchema: The created project.
    """
    return ProjectController.create_new_project(project_title=project.project_title,
                                                project_description=project.project_description,
                                                due_date=project.due_date,
                                                generation_id=project.generation_id)


@project_router.get("/get-all-projects", response_model=list[ProjectSchema])
def get_all_projects():
    """
    Retrieve all projects.

    Returns: List[ProjectSchema]: A list of all projects.
    """
    return ProjectController.get_all_projects()


@project_router.get("/get-project-by-id", response_model=ProjectSchema)
def get_project_by_id(project_id: str):
    """
    Retrieve a project by its ID.

    Args: project_id (str): The ID of the project to retrieve.

    Returns: ProjectSchema: The project with the specified ID.
    """
    return ProjectController.get_project_by_id(project_id=project_id)


@project_router.get("/get-project-by-title", response_model=list[ProjectSchema])
def get_project_by_title(project_title: str):
    """
    Retrieve a project or projects by its title.

    Args: project_title (str): The title of the project to retrieve.

    Returns: List[ProjectSchema]: A list of projects with the specified title or part of the title.
        """
    return ProjectController.get_project_by_title(project_title=project_title)


@project_router.put("/update-project", response_model=ProjectSchema)
def update_project_by_id(project_id: str, project: ProjectSchemaUpdate):
    """
    Update a project with the specified ID.

    Args:
        project_id (str): The ID of the project to update.
        project (ProjectSchemaUpdate): The updated project information.

    Returns: ProjectSchema: The updated project.
    """
    project_dict = {attr: value for attr, value in project.dict().items() if value}
    return ProjectController.update_project_by_id(project_id=project_id, project=project_dict)


@project_router.delete("/delete-project")
def delete_project_by_id(project_id: str):
    """
    Delete a project with the specified ID.

    Args: project_id (str): The ID of the project to delete.

    Returns: str: A message indicating the success of the operation.
    """
    return ProjectController.delete_project_by_id(project_id=project_id)


# Project Task Router starts here
project_task_router = APIRouter(prefix="/api/project-tasks", tags=["Project Tasks"])


@project_task_router.post("/add-new-project-task", response_model=ProjectTaskSchema)
def create_new_project_task(project_task: ProjectTaskSchemaIn):
    """
    Create a new project task with the specified project task details.

    Args: project_task (ProjectTaskSchemaIn): The project task details.

    Returns: ProjectTaskSchema: The created project task.
    """
    return ProjectTaskController.create_new_project_task(task_number=project_task.task_number,
                                                         task_description=project_task.task_description,
                                                         task_max_points=project_task.task_max_points,
                                                         project_id=project_task.project_id)


@project_task_router.get("/get-all-project-tasks", response_model=list[ProjectTaskSchema])
def get_all_project_tasks():
    """
    Retrieve all project tasks.

    Returns: List[ProjectTaskSchema]: A list of all project tasks.
    """
    return ProjectTaskController.get_all_project_tasks()


@project_task_router.get("/get-project-task-by-id", response_model=ProjectTaskSchema)
def get_project_task_by_id(project_task_id: str):
    """
    Retrieve a project task by its ID.

    Args: project_task_id (str): The ID of the project task to retrieve.

    Returns: ProjectTaskSchema: The project task with the specified ID.
    """
    return ProjectTaskController.get_project_task_by_id(project_task_id=project_task_id)


@project_task_router.get("/get-project-task-by-number", response_model=ProjectTaskSchema)
def get_project_task_by_number(task_number: int):
    """
    Retrieve a project task by its number.

    Args: task_number (int): The number of the project task to retrieve.

    Returns: ProjectSchema: The project task with specified task number.
    """
    return ProjectTaskController.get_project_task_by_number(task_number)


@project_task_router.get("/get-project-task-by-min-points", response_model=list[ProjectTaskSchema])
def get_project_task_by_min_points(min_points: int):
    """
    Retrieve a project task or project tasks with more or equal points than provided.

    Args: min_points (int): Minimum points for project task.

    Returns: List[ProjectTaskSchema]: A list of project tasks with more or equal points than provided min points.
        """
    return ProjectTaskController.get_project_task_by_min_points(min_points=min_points)


@project_task_router.put("/update-project-task", response_model=ProjectTaskSchema)
def update_project_task_by_id(project_task_id: str, project_task: ProjectTaskSchemaUpdate):
    """
    Update a project task with the specified ID.

    Args:
        project_task_id (str): The ID of the project task to update.
        project_task (ProjectTaskSchemaUpdate): The updated project task information.

    Returns: ProjectTaskSchema: The updated project task.
    """
    project_task_dict = {attr: value for attr, value in project_task.dict().items() if value}
    return ProjectTaskController.update_project_task_by_id(project_task_id=project_task_id,
                                                           project_task=project_task_dict)


@project_task_router.delete("/delete-project-task")
def delete_project_task_by_id(project_task_id: str):
    """
    Delete a project task with the specified ID.

    Args: project_task_id (str): The ID of the project task to delete.

    Returns: str: A message indicating the success of the operation.
    """
    return ProjectTaskController.delete_project_task_by_id(project_task_id=project_task_id)

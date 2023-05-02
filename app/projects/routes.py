from fastapi import APIRouter

from app.projects.controller import ProjectController
from app.projects.schemas import ProjectSchema, ProjectSchemaIn, ProjectSchemaUpdate

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

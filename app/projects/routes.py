from fastapi import APIRouter

from app.projects.controller import ProjectController
from app.projects.schemas import ProjectSchema, ProjectSchemaIn

project_router = APIRouter(prefix="/api/projects", tags=["Projects"])


@project_router.post("/add-new-project", response_model=ProjectSchema)
def create_new_project(project: ProjectSchemaIn):
    return ProjectController.create_new_project(project_title=project.project_title,
                                                project_description=project.project_description,
                                                due_date=project.due_date,
                                                generation_id=project.generation_id)

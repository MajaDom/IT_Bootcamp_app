from fastapi import APIRouter
from app.user_projects.controller import UserProjectsController
from app.user_projects.schemas import *
# from app.user.controller.user_authenification_controller import JWTBearer

user_projects_router = APIRouter(tags=["user-projects"], prefix="/api/user-projects")


@user_projects_router.post("/add-new-user-projects", response_model= UserProjectsSchema)
def create_user_projects(user_projects: UserProjectsSchemaIn):
    return UserProjectsController.create_user_projects(user_projects.name, user_projects.scope, user_projects.link, user_projects.file, user_projects.status, user_projects.additional) #to add user_generation_id after its been done

@user_projects_router.get("/id", response_model=UserProjectsSchema)
def get_user_projects_by_id(user_projects_id: str):
    return UserProjectsController.get_user_projects_by_id(user_projects_id)    

@user_projects_router.get("/get-user-projects-by-name", response_model=UserProjectsSchema)
def get_user_projects_by_name(user_projects_name: str):
    return UserProjectsController.get_user_projects_by_name(user_projects_name)  

@user_projects_router.get("/get-all-user-projects", response_model=list[UserProjectsSchema])
def get_all_user_projects():
    return UserProjectsController.get_all_user_projects()

@user_projects_router.patch("/update-user-projects", response_model = UserProjectsSchema) 
def update_user_projects_by_id(user_projects_id: str, user_projects: UpdateUserProjectsSchemaIn):
    return UserProjectsController.update_user_project_by_id(user_projects_id, user_projects)

@user_projects_router.delete("/")
def delete_user_projects_by_id(user_projects_id: str):
    return UserProjectsController.delete_user_projects_by_id(user_projects_id)

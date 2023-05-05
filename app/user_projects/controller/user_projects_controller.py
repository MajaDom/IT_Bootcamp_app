from app.user_projects.services import UserProjectsServices
from app.user_projects.exceptions import UserProjectNotFound, UserProjectExists
from fastapi import HTTPException, Response


class UserProjectsController:

    @staticmethod
    def create_user_projects(name: str, scope: str, link: str, file: bytes, status: str, additional: str): #to do: to add user_generation_id
        try:
            user_projects = UserProjectsServices.create_user_projects(name, scope, link, file, status, additional) #to do: to add user_generation_id   
            return user_projects

        except UserProjectExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_projects_by_id(user_projects_id: str):
        try:
            user_projects = UserProjectsServices.get_user_projects_by_id(user_projects_id) 
            if user_projects:
                return user_projects
        except UserProjectNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_projects_by_name(user_projects_name: str):
        try:
            user_projects = UserProjectsServices.get_user_projects_by_name(user_projects_name)
            if user_projects:
                return user_projects
        except UserProjectNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_user_projects():
        user_projects = UserProjectsServices.get_all_user_projects()
        return user_projects
    

    @staticmethod
    def update_user_project_by_id(user_projects_id: str, user_projects):
  
        try:
            UserProjectsServices.update_user_projects_by_id(user_projects_id, user_projects)        
            return Response(content=f"User Projects with id - {user_projects_id} is updated")
        except UserProjectNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @staticmethod
    def delete_user_projects_by_id(user_projects_id: str):
        try:
            UserProjectsServices.delete_user_projects_by_id(user_projects_id)     
            return Response(content=f"User Projects with id - {user_projects_id} is deleted")
        except UserProjectNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

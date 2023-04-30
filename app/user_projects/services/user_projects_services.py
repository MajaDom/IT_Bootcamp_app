from app.db.database import SessionLocal
from app.user_projects.repository import UserProjectsRepository
from app.user_projects.models import UserProjects
from app.user_projects.exceptions import UserProjectNotFound
from app.user_projects.schemas import UpdateUserProjectsSchemaIn
from fastapi.encoders import jsonable_encoder

class UserProjectsServices:

    @staticmethod
    def create_user_projects(name: str, scope: str, link: str, file: bytes, status: str, additional: str): #to do: to add user_generation_id
        with SessionLocal() as db:
            try:
                user_projects_repository = UserProjectsRepository(db, UserProjects)
                fields = {"name": name, "scope": scope, "link": link, "file": file, "status": status, "additional": additional,}
                obj = user_projects_repository.create(fields)
                return obj       
            except Exception as e:
                raise e


    @staticmethod
    def get_user_projects_by_id(user_projects_id: str):
        with SessionLocal() as db:
            try:
                user_projects_repository = UserProjectsRepository(db, UserProjects)
                return user_projects_repository.get_user_projects_by_id(user_projects_id)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_user_projects_by_name(user_projects_name: str):
        with SessionLocal() as db:
            try:
                user_projects_repository = UserProjectsRepository(db, UserProjects)
                return user_projects_repository.get_user_projects_by_name(user_projects_name=user_projects_name)
            except Exception as e:
                raise e


    @staticmethod
    def get_all_user_projects():
        with SessionLocal() as db:
            user_projects_repository = UserProjectsRepository(db, UserProjects)
            return user_projects_repository.get_all_user_projects()


    @staticmethod
    def update_user_projects_by_id(user_projects_id: str, user_projects):
        try:
            with SessionLocal() as db:
                user_projects_repository = UserProjectsRepository(db, UserProjects)
                stored_user_projects_data = user_projects_repository.get_user_projects_by_id(
                    user_projects_id)
                if not stored_user_projects_data:
                    raise UserProjectNotFound(message="Generation not found.", code=404)
                stored_user_projects_model = UpdateUserProjectsSchemaIn(
                    **jsonable_encoder(stored_user_projects_data))
                update_data = user_projects.dict(exclude_unset=True)
                updated_user_projects = stored_user_projects_model.copy(
                    update=update_data)
                return user_projects_repository.update_user_projects_by_id(user_projects_id, updated_user_projects.name, updated_user_projects.scope, updated_user_projects.link, updated_user_projects.file, updated_user_projects.status, updated_user_projects.additional)
        except Exception as e:
            raise e


    @staticmethod
    def delete_user_projects_by_id(user_projects_id: str):
        try:
            with SessionLocal() as db:
                user_projects_repository = UserProjectsRepository(db, UserProjects)
                return user_projects_repository.delete_user_projects_by_id(user_projects_id)
        except Exception as e:
            raise e


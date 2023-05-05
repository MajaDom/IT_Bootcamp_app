from sqlalchemy.exc import IntegrityError
from app.user_projects.models import UserProjects
from app.user_projects.exceptions import UserProjectNotFound
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException

class UserProjectsRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="User Project with this id is already registered.", code=400) from exc


    def get_user_projects_by_id(self, user_projects_id: str):
        user_projects = self.db.query(UserProjects).filter(UserProjects.id == user_projects_id).first()
        return user_projects
    
    def get_user_projects_by_name(self, user_projects_name: str):

        user_projects = self.db.query(UserProjects).filter(UserProjects.name == user_projects_name).first()
        if user_projects is None:
            raise UserProjectNotFound(f"User Project with provided name: {user_projects_name} not found.", 404)
        return user_projects


    def get_all_user_projects(self):
        user_projects = self.db.query(UserProjects).all()
        return user_projects
    
    

    def update_user_projects_by_id(self, user_projects_id, name: str, scope: str, link: str, file: bytes, status: str, additional: str): #to do: to add user_generation_id
                                  
            try:
                user_projects = self.db.query(UserProjects).filter(UserProjects.id == user_projects_id).first()
                user_projects.name = name
                user_projects.scope = scope
                user_projects.link = link
                user_projects.file = file
                user_projects.status = status
                user_projects.additional = additional
                self.db.add(user_projects)
                self.db.commit()
                self.db.refresh(user_projects)
                return user_projects
            except IntegrityError as e:
                raise e


    def delete_user_projects_by_id(self, user_projects_id: str):
        try:
            user_projects = self.db.query(UserProjects).filter(UserProjects.id == user_projects_id).first()
            self.db.delete(user_projects)
            self.db.commit()
            return True
        except Exception as e:
            raise e


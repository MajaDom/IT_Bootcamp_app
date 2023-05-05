from sqlalchemy.exc import IntegrityError
from app.user_generation.models import UserGeneration
from app.user_generation.exceptions import UserGenerationNotFound
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException

class UserGenerationRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Generation with this id is already registered.", code=400) from exc



    def get_user_generation_by_id(self, user_generation_id: str):
        user_generation = self.db.query(UserGeneration).filter(UserGeneration.id == user_generation_id).first()
        return user_generation
    
    def get_all_user_generations(self):
        user_generations = self.db.query(UserGeneration).all()
        return user_generations
    

    def update_user_generation_by_id(self, user_generation_id, activated_date, deactivated_date, is_active, description, user_id, generation_id):
            try:
                user_generation = self.db.query(UserGeneration).filter(UserGeneration.id == user_generation_id).first()
                user_generation.activated_date = activated_date
                user_generation.deactivated_date = deactivated_date
                user_generation.is_active = is_active
                user_generation.description = description
                user_generation.user_id = user_id
                user_generation.generation_id = generation_id
                self.db.add(user_generation)
                self.db.commit()
                self.db.refresh(user_generation)
                return user_generation
            except IntegrityError as e:
                raise e


    def delete_user_generation_by_id(self, user_generation_id: str):
        try:
            user_generation = self.db.query(UserGeneration).filter(UserGeneration.id == user_generation_id).first()
            self.db.delete(user_generation)
            self.db.commit()
            return True
        except Exception as e:
            raise e


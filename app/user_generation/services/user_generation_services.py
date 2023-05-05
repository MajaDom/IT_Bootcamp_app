from app.db.database import SessionLocal
from app.user_generation.repository import UserGenerationRepository
from app.user_generation.models import UserGeneration
from app.user_generation.exceptions import UserGenerationNotFound
from app.user_generation.schemas import UpdateUserGenerationSchemaIn
from fastapi.encoders import jsonable_encoder

class UserGenerationServices:

    @staticmethod
    def create_user_generation(activated_date, deactivated_date, is_active, description, user_id, generation_id):
        with SessionLocal() as db:
            try:
                user_generation_repository = UserGenerationRepository(db, UserGeneration)
                fields = {"activated_date": activated_date, "deactivated_date": deactivated_date, "is_active": is_active, "description": description, "user_id": user_id, "generation_id": generation_id}
                obj = user_generation_repository.create(fields)
                return obj       
            except Exception as e:
                raise e


    @staticmethod
    def get_user_generation_by_id(user_generation_id: str):
        with SessionLocal() as db:
            try:
                user_generation_repository = UserGenerationRepository(db, UserGeneration)
                return user_generation_repository.get_user_generation_by_id(user_generation_id)
            except Exception as e:
                raise e
            

    @staticmethod
    def get_all_user_generations():
        with SessionLocal() as db:
            user_generation_repository = UserGenerationRepository(db, UserGeneration)
            return user_generation_repository.get_all_user_generations()


    @staticmethod
    def update_user_generation_by_id(user_generation_id: str, user_generation):
        try:
            with SessionLocal() as db:
                user_generation_repository = UserGenerationRepository(db, UserGeneration)
                stored_user_generation_data = user_generation_repository.get_user_generation_by_id(
                    user_generation_id)
                if not stored_user_generation_data:
                    raise UserGenerationNotFound(message="Generation not found.", code=404)
                stored_user_generation_model = UpdateUserGenerationSchemaIn(
                    **jsonable_encoder(stored_user_generation_data))
                update_data = user_generation.dict(exclude_unset=True)
                updated_user_generation = stored_user_generation_model.copy(
                    update=update_data)
                return user_generation_repository.update_user_generation_by_id(user_generation_id, updated_user_generation.activated_date, updated_user_generation.deactivated_date, updated_user_generation.is_active, updated_user_generation.description, updated_user_generation.user_id, updated_user_generation.generation_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_user_generation_by_id(user_generation_id: str):
        try:
            with SessionLocal() as db:
                user_generation_repository = UserGenerationRepository(db, UserGeneration)
                return user_generation_repository.delete_user_generation_by_id(user_generation_id)
        except Exception as e:
            raise e




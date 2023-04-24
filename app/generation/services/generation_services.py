from app.db.database import SessionLocal
from app.generation.repository import GenerationRepository
from app.generation.models import Generation
from app.generation.exceptions import GenerationNotFound
from app.generation.schemas import UpdateGenerationSchemaIn
from fastapi.encoders import jsonable_encoder

class GenerationServices:

    @staticmethod
    def create_generation(name, start_date, end_date, is_active, course_id):
        with SessionLocal() as db:
            try:
                generation_repository = GenerationRepository(db, Generation)
                fields = {"name": name, "start_date": start_date, "end_date": end_date, "is_active": is_active, "course_id": course_id}
                obj = generation_repository.create(fields)
                return obj       
            except Exception as e:
                raise e


    @staticmethod
    def get_generation_by_id(generation_id: str):
        with SessionLocal() as db:
            try:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.get_generation_by_id(generation_id)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_generation_by_name(generation_name: str):
        with SessionLocal() as db:
            try:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.get_generation_by_name(generation_name=generation_name)
            except Exception as e:
                raise e


    @staticmethod
    def get_all_generations():
        with SessionLocal() as db:
            generation_repository = GenerationRepository(db, Generation)
            return generation_repository.get_all_generations()


    @staticmethod
    def update_generation_by_id(generation_id: str, generation):
        try:
            with SessionLocal() as db:
                generation_repository = GenerationRepository(db)
                stored_generation_data = generation_repository.get_generation_by_id(
                    generation_id)
                if not stored_generation_data:
                    raise GenerationNotFound(message="Generation not found.", code=404)
                stored_generation_model = UpdateGenerationSchemaIn(
                    **jsonable_encoder(stored_generation_data))
                update_data = generation.dict(exclude_unset=True)
                updated_generation = stored_generation_model.copy(
                    update=update_data)
                return generation_repository.update_generation_by_id(generation_id, updated_generation.name, updated_generation.start_date, updated_generation.end_date, updated_generation.is_active, updated_generation.course_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_generation_by_id(generation_id: str):
        try:
            with SessionLocal() as db:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.delete_generation_by_id(generation_id)
        except Exception as e:
            raise e


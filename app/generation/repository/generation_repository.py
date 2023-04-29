from sqlalchemy.exc import IntegrityError
from app.generation.models import Generation
from app.generation.exceptions import GenerationNotFound
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException

class GenerationRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Generation with this id is already registered.", code=400) from exc



    def get_generation_by_id(self, generation_id: str):
        generation = self.db.query(Generation).filter(Generation.id == generation_id).first()
        return generation
    
    def get_generation_by_name(self, generation_name: str):

        generation = self.db.query(Generation).filter(Generation.name == generation_name).first()
        if generation is None:
            raise GenerationNotFound(f"Generation with provided name: {generation_name} not found.", 404)
        return generation


    def get_all_generations(self):
        generations = self.db.query(Generation).all()
        return generations
    

    def update_generation_by_id(self, generation_id, name, start_date, end_date, is_active, course_id):
            try:
                generation = self.db.query(Generation).filter(Generation.id == generation_id).first()
                generation.name = name
                generation.start_date = start_date
                generation.end_date = end_date
                generation.is_active = is_active
                generation.course_id = course_id
                self.db.add(generation)
                self.db.commit()
                self.db.refresh(generation)
                return generation
            except IntegrityError as e:
                raise e


    def delete_generation_by_id(self, generation_id: str):
        try:
            generation = self.db.query(Generation).filter(Generation.id == generation_id).first()
            self.db.delete(generation)
            self.db.commit()
            return True
        except Exception as e:
            raise e
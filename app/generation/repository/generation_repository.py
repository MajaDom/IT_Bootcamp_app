from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
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



    # def create_generation(self, name, start_date, end_date, is_active, course_id):
    #     """
    #     This function creates a new generation object with the given parameters and adds it to the
    #     database.
        
    #     :param name: The name of the generation being created
    #     :param start_date: The start date of the generation, which is the date when the generation
    #     begins. It is usually a datetime object or a string in a specific format that can be parsed into
    #     a datetime object
    #     :param end_date: The end date of the generation being created. This is the date when the
    #     generation will come to an end
    #     :param is_active: is_active is a boolean parameter that indicates whether the generation is
    #     currently active or not. If it is set to True, it means the generation is currently active, and
    #     if it is set to False, it means the generation is not active
    #     :param course_id: The course_id parameter is the unique identifier of the course to which the
    #     generation belongs. It is used to associate the generation with the corresponding course in the
    #     database
    #     :return: an instance of the `Generation` class that has been created and added to the database.
    #     """
    #     #TO DO: to add exception if generation with name, start date, end date already exists
    #     try:
    #         generation = Generation(name, start_date, end_date, is_active, course_id)
    #         self.db.add(generation)
    #         self.db.commit()
    #         self.db.refresh(generation)
    #         return generation
    #     except IntegrityError as e:
    #         raise e


    def get_generation_by_id(self, generation_id: str):
        user = self.db.query(Generation).filter(Generation.id == generation_id).first()
        return user
    
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
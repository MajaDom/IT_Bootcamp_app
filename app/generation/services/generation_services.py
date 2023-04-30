from app.db.database import SessionLocal
from app.generation.repository import GenerationRepository
from app.generation.models import Generation
from app.generation.exceptions import GenerationNotFound
from app.generation.schemas import UpdateGenerationSchemaIn
from fastapi.encoders import jsonable_encoder

class GenerationServices:

    @staticmethod
    def create_generation(name, start_date, end_date, is_active, course_id):
        """
        This function creates a new generation object with the given parameters and saves it to the
        database.
        :return: an object of the newly created generation.
        """
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
        """
        This function retrieves a generation object from the database by its ID.
        
        :param generation_id: The generation_id parameter is a string that represents the unique
        identifier of a generation in a database. This function retrieves the generation object
        associated with the given generation_id from the database using the GenerationRepository class
        :type generation_id: str
        :return: The function `get_generation_by_id` returns the generation object with the specified
        `generation_id` from the database. If the generation is not found or an error occurs, an
        exception is raised.
        """
        with SessionLocal() as db:
            try:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.get_generation_by_id(generation_id)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_generation_by_name(generation_name: str):
        """
        This function retrieves a generation object from the database by its name.
        
        :param generation_name: A string representing the name of a generation. This function retrieves
        a generation object from the database based on the provided name
        :type generation_name: str
        :return: The function `get_generation_by_name` returns the generation object with the given
        `generation_name` parameter from the database using the `GenerationRepository` class. If there
        is an error, it raises an exception.
        """
        with SessionLocal() as db:
            try:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.get_generation_by_name(generation_name=generation_name)
            except Exception as e:
                raise e


    @staticmethod
    def get_all_generations():
        """
        This function retrieves all generations from a database using a repository pattern.
        :return: all generations from the database using the `get_all_generations()` method of the
        `GenerationRepository` class.
        """
        with SessionLocal() as db:
            generation_repository = GenerationRepository(db, Generation)
            return generation_repository.get_all_generations()



    @staticmethod
    def update_generation_by_id(generation_id: str, generation):
        """
        This function updates a generation in the database by its ID.
        
        :param generation_id: A string representing the unique identifier of a generation
        :type generation_id: str
        :param generation: It is a parameter of an unspecified type that represents the updated
        generation data that will be used to update the existing generation in the database
        :return: the result of calling the `update_generation_by_id` method of the
        `generation_repository` object with the updated generation data.
        """
        try:
            with SessionLocal() as db:
                generation_repository = GenerationRepository(db, Generation)
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
        """
        This function deletes a generation from the database by its ID.
        
        :param generation_id: A string representing the unique identifier of a generation that needs to
        be deleted from the database
        :type generation_id: str
        :return: the result of calling the `delete_generation_by_id` method of a `GenerationRepository`
        object, which is deleting a generation from the database based on the provided `generation_id`.
        """
        try:
            with SessionLocal() as db:
                generation_repository = GenerationRepository(db, Generation)
                return generation_repository.delete_generation_by_id(generation_id)
        except Exception as e:
            raise e


from sqlalchemy.exc import IntegrityError
from app.generation.models import Generation
from app.generation.exceptions import GenerationNotFound
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException

class GenerationRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        """
        This function creates a new object with the given attributes, but if there is an integrity error
        (such as a duplicate id), it rolls back the transaction and raises an exception.
        
        :param attributes: A dictionary containing the attributes of the object being created. This is
        being passed to a method that creates a new object in a database or other data store. If
        the creation is successful, the method returns the newly created object.
        :type attributes: dict
        :return: The `create` method is returning the result of calling the `create` method of the
        parent class (using `super().create(attributes)`). If there is an `IntegrityError` raised during
        this call, the method catches it, rolls back the database transaction, and raises an
        `AppException` with a custom error message and status code.
        """
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Generation with this id is already registered.", code=400) from exc

    def get_generation_by_id(self, generation_id: str):
        """
        This function retrieves a generation object from a database based on its ID.
        
        :param generation_id: The generation_id parameter is a string that represents the unique
        identifier of a generation in a database. The function retrieves the generation object from the
        database that matches the provided generation_id
        :type generation_id: str
        :return: an instance of the `Generation` class that matches the provided `generation_id`.
        """
        generation = self.db.query(Generation).filter(Generation.id == generation_id).first()
        return generation
    
    def get_generation_by_name(self, generation_name: str):
        """
        This function retrieves a generation object from a database based on its name and raises an
        exception if it is not found.
        
        :param generation_name: A string representing the name of a generation
        :type generation_name: str
        :return: The function `get_generation_by_name` returns a `Generation` object from the database
        that matches the provided `generation_name` parameter. If no matching `Generation` object is
        found, it raises a `GenerationNotFound` exception with a message indicating that the generation
        with the provided name was not found.
        """

        generation = self.db.query(Generation).filter(Generation.name == generation_name).first()
        if generation is None:
            raise GenerationNotFound(f"Generation with provided name: {generation_name} not found.", 404)
        return generation


    def get_all_generations(self):
        """
        This function retrieves all generations from a database and returns them.
        :return: The function `get_all_generations` is returning a list of all the `Generation` objects
        stored in the database.
        """
        generations = self.db.query(Generation).all()
        return generations
    

    def update_generation_by_id(self, generation_id, name, start_date, end_date, is_active, course_id):
        """
        This function updates a generation's information in a database by its ID.
        
        :param generation_id: The unique identifier of the generation that needs to be updated
        :param name: The name of the generation
        :param start_date: The start date of the generation
        :param end_date: The end date of the generation
        :param is_active: A boolean value indicating whether the generation is currently active or not.
        If True, it means the generation is currently ongoing, while if False, it means the generation
        has ended
        :param course_id: The ID of the course that the generation belongs to
        :return: the updated Generation object.
        """
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
        """
        This function deletes a generation from a database based on its ID.
        
        :param generation_id: The generation_id parameter is a string that represents the unique
        identifier of a generation in a database. This function deletes the generation with the
        specified generation_id from the database
        :type generation_id: str
        :return: a boolean value of True if the generation with the given generation_id is successfully
        deleted from the database, and raising an exception if there is an error during the deletion
        process.
        """
        try:
            generation = self.db.query(Generation).filter(Generation.id == generation_id).first()
            self.db.delete(generation)
            self.db.commit()
            return True
        except Exception as e:
            raise e
from app.generation.services import GenerationServices
from app.generation.exceptions import GenerationNotFound, GenerationExists
from fastapi import HTTPException, Response



class GenerationController:

    @staticmethod
    def create_generation(name, start_date, end_date, is_active, course_id):
        """
        This function creates a new generation with the given parameters and returns it, handling
        exceptions if necessary.
        
        :param name: The name of the generation being created
        :param start_date: The start date of the generation, which is the date when the course will
        begin
        :param end_date: The end date of a generation, which is the date when the generation will be
        completed or finished
        :param is_active: is_active is a boolean parameter that indicates whether the generation is
        currently active or not. If it is set to True, it means the generation is currently active, and
        if it is set to False, it means the generation is not currently active
        :param course_id: The course_id parameter is an identifier for the course that the generation
        belongs to. It is used to associate the generation with a specific course in the system
        :return: the generation object created by the `GenerationServices.create_generation()` method.
        """
        try:
            generation = GenerationServices.create_generation(name, start_date, end_date, is_active, course_id)      
            return generation

        except GenerationExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_generation_by_id(generation_id: str):
        """
        This function retrieves a generation by its ID and raises an exception if it is not found or if
        there is an internal server error.
        
        :param generation_id: a string representing the unique identifier of a generation
        :type generation_id: str
        :return: the generation object retrieved from the `GenerationServices` class by its ID, if it
        exists. If the generation is not found, it raises an HTTPException with the corresponding error
        code and message. If any other exception occurs, it raises an HTTPException with a 500 error
        code and the exception message.
        """
        try:
            generation = GenerationServices.get_generation_by_id(generation_id) 
            if generation:
                return generation
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_generation_by_name(generation_name: str):
        """
        This function retrieves a generation by its name and raises an exception if it is not found or
        if there is an internal server error.
        
        :param generation_name: a string representing the name of a generation
        :type generation_name: str
        :return: the generation object if it exists, otherwise it will raise an HTTPException with a
        status code and detail message.
        """
        try:
            generation = GenerationServices.get_generation_by_name(generation_name)
            if generation:
                return generation
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_all_generations():
        """
        This function retrieves all generations using a service called GenerationServices.
        :return: a list of all generations. The exact format and content of the list will depend on the
        implementation of the `GenerationServices.get_all_generations()` method.
        """
        generations = GenerationServices.get_all_generations()
        return generations
    

    @staticmethod
    def update_generation_by_id(generation_id: str, generation):
        """
        This function updates a generation by its ID and returns a response message.
        
        :param generation_id: a string representing the unique identifier of a generation object
        :type generation_id: str
        :param generation: It is a variable that contains the updated generation data that needs to be
        saved in the database. The data could include attributes such as generation name, description,
        start date, end date, etc
        :return: a `Response` object with a message indicating that the generation with the given ID has
        been updated.
        """
  
        try:
            GenerationServices.update_generation_by_id(generation_id, generation)        
            return Response(content=f"Generation with id - {generation_id} is updated")
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @staticmethod
    def delete_generation_by_id(generation_id: str):
        """
        This function deletes a generation by its ID and returns a response message.
        
        :param generation_id: a string representing the unique identifier of a generation that needs to
        be deleted. The function uses this ID to call a service method that deletes the corresponding
        generation from a database or any other data storage. If the generation is successfully deleted,
        the function returns a response message confirming the deletion. If the generation is
        :type generation_id: str
        :return: a FastAPI Response object with a message indicating that a generation with the
        specified ID has been deleted. If the generation is not found, a custom HTTPException is raised
        with a specific error message. If any other exception occurs, a generic HTTPException is raised
        with the error message converted to a string.
        """
        try:
            GenerationServices.delete_generation_by_id(generation_id)     
            return Response(content=f"Generation with id - {generation_id} is deleted")
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))




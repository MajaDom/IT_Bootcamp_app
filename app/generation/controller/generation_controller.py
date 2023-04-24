from app.generation.services import GenerationServices
from app.generation.exceptions import GenerationNotFound, GenerationExists
from fastapi import HTTPException, Response


class GenerationController:

    @staticmethod
    def create_generation(name, start_date, end_date, is_active, course_id):
        try:
            generation = GenerationServices.create_generation(name, start_date, end_date, is_active, course_id)      
            return generation

        except GenerationExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_generation_by_id(generation_id: str):
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
        generations = GenerationServices.get_all_generations()
        return generations
    

    @staticmethod
    def update_generation_by_id(generation_id: str, generation):
  
        try:
            GenerationServices.update_generation_by_id(generation_id, generation)        
            return Response(content=f"Generation with id - {generation_id} is updated")
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @staticmethod
    def delete_generation_by_id(generation_id: str):
        try:
            GenerationServices.delete_generation_by_id(generation_id)     
            return Response(content=f"Generation with id - {generation_id} is deleted")
        except GenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))




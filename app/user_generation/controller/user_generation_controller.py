from app.user_generation.services import UserGenerationServices
from app.user_generation.exceptions import UserGenerationNotFound, UserGenerationExists
from fastapi import HTTPException, Response


class UserGenerationController:

    @staticmethod
    def create_user_generation(activated_date, deactivated_date, is_active, description, user_id, generation_id):
        try:
            user_generation = UserGenerationServices.create_user_generation(activated_date, deactivated_date, is_active, description, user_id, generation_id)      
            return user_generation

        except UserGenerationExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_generation_by_id(user_generation_id: str):
        try:
            user_generation = UserGenerationServices.get_user_generation_by_id(user_generation_id) 
            if user_generation:
                return user_generation
        except UserGenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_all_user_generations():
        user_generations = UserGenerationServices.get_all_user_generations()
        return user_generations
    

    @staticmethod
    def update_user_generation_by_id(user_generation_id: str, user_generation):
  
        try:
            UserGenerationServices.update_user_generation_by_id(user_generation_id, user_generation)        
            return Response(content=f"User Generation with id - {user_generation_id} is updated")
        except UserGenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @staticmethod
    def delete_user_generation_by_id(user_generation_id: str):
        try:
            UserGenerationServices.delete_user_generation_by_id(user_generation_id)     
            return Response(content=f"User Generation with id - {user_generation_id} is deleted")
        except UserGenerationNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



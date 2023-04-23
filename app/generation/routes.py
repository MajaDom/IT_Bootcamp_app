from fastapi import APIRouter, Depends
from app.generation.controller import GenerationController
from app.generation.schemas import *
# from app.user.controller.user_authenification_controller import JWTBearer

generation_router = APIRouter(tags=["generation"], prefix="/api/generation")


@generation_router.post("/add-new-generation", response_model= GenerationSchema)
def create_generation(generation: GenerationSchemaIn):
    return GenerationController.create_generation(generation.name, generation.start_date, generation.end_date, generation.is_active, generation.course_id) 


@generation_router.get("/id", response_model=GenerationSchema)
def get_generation_by_id(generation_id: str):
    return GenerationController.get_generation_by_id(generation_id)    

@generation_router.get("/get-generation_by_name", response_model=GenerationSchema)
def get_generation_by_name(generation_name: str):
    return GenerationController.get_generation_by_name(generation_name)  

@generation_router.get("/get-all-generations", response_model=GenerationSchema)
def get_all_generations():
    return GenerationController.get_all_generations()

@generation_router.patch("/update-generation", response_model = GenerationSchema) 
def update_generation_by_id(generation_id: str, generation: UpdateGenerationSchemaIn):
    return GenerationController.update_generation_by_id(generation_id, generation)

@generation_router.delete("/")
def delete_generation_by_id(generation_id: str):
    return GenerationController.delete_generation_by_id(generation_id)      

from fastapi import APIRouter
from app.user_generation.controller.user_generation_controller import UserGenerationController 
from app.user_generation.schemas import UserGenerationSchema, UserGenerationSchemaIn, UpdateUserGenerationSchemaIn


user_generation_router = APIRouter(tags=["user-generation"], prefix="/api/user-generation")


@user_generation_router.post("/add-new-user-generation", response_model= UserGenerationSchema)
def create_user_generation(user_generation: UserGenerationSchemaIn):
    return UserGenerationController.create_user_generation(user_generation.activated_date, user_generation.deactivated_date, user_generation.is_active, user_generation.description, user_generation.user_id, user_generation.generation_id) 

@user_generation_router.get("/id", response_model=UserGenerationSchema)
def get_user_generation_by_id(user_generation_id: str):
    return UserGenerationController.get_user_generation_by_id(user_generation_id)    

@user_generation_router.get("/get-all-user-generations", response_model=list[UserGenerationSchema])
def get_all_user_generations():
    return UserGenerationController.get_all_user_generations()

@user_generation_router.patch("/update-user-generation", response_model = UserGenerationSchema) 
def update_generation_by_id(user_generation_id: str, user_generation: UpdateUserGenerationSchemaIn):
    return UserGenerationController.update_user_generation_by_id(user_generation_id, user_generation)

@user_generation_router.delete("/")
def delete_user_generation_by_id(user_generation_id: str):
    return UserGenerationController.delete_user_generation_by_id(user_generation_id)

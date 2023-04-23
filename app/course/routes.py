from fastapi import APIRouter, Depends
from app.course.controller import CourseController
from app.course.schemas import *
# from app.user.controller.user_authenification_controller import JWTBearer

course_router = APIRouter(tags=["course"], prefix="/api/course")


@course_router.post("/add-new-course", response_model= CourseSchema)
def create_course(course: CourseSchemaIn):
    return CourseController.create_course(course.course_name, course.course_description) 


@course_router.get("/id", response_model=CourseSchema)
def get_course_by_id(course_id: str):
    return CourseController.get_course_by_id(course_id)    


@course_router.get("/get-all-contact-types", response_model=CourseSchema)
def get_all_courses():
    return CourseController.get_all_courses()

@course_router.delete("/")
def delete_course_by_id(course_id: str):
    return CourseController.delete_course_by_id(course_id)      

@course_router.put("/update", response_model=CourseSchema)
<<<<<<< Updated upstream
def update_course(course_id, new_course):
    return CourseController.update_course(course_id, new_course)
=======
def update_course(course_id, new_name):
    return CourseController.update_course_name(course_id, new_name)

>>>>>>> Stashed changes

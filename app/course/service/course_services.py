from app.course.repository import CourseRepository
from app.db.database import SessionLocal
from app.course.exceptions import CourseNotFound
from app.course.models import Course
from app.course.schemas import UpdateCourseSchemaIn
from fastapi.encoders import jsonable_encoder

class CourseServices:
    @staticmethod
    def create_course(course_name, course_description):
        with SessionLocal() as db:
            try:
                course_repository = CourseRepository(db, Course)
                fields = {"course_name": course_name, "course_description": course_description}
                obj = course_repository.create(fields)
                return obj       
            except Exception as e:
                raise e


    @staticmethod
    def get_course_by_id(course_id: str):

        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db)
                return course_repository.get_course_by_id(course_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_courses():

        with SessionLocal() as db:
            course_repository = CourseRepository(db)
            return course_repository.get_all_courses()



    # @staticmethod
    # def update_course_name(course_id: str, new_name: str):
    #     try:
    #         with SessionLocal() as db:
    #             course_repository = CourseRepository(db)                  
    #             return course_repository.update_course_name(course_id, new_name)          
    #     except Exception as e:
    #         raise e

    @staticmethod
    def update_course_by_id(course_id: str, course):
        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db, Course)
                stored_course_data = course_repository.get_course_by_id(
                    course_id)
                if not stored_course_data:
                    raise CourseNotFound(message="Course not found.", code=404)
                stored_course_model = UpdateCourseSchemaIn(
                    **jsonable_encoder(stored_course_data))
                update_data = course.dict(exclude_unset=True)
                updated_course = stored_course_model.copy(
                    update=update_data)
                return course_repository.update_course_by_id(course_id, updated_course.course_name, updated_course.course_description)
        except Exception as e:
            raise e
        
    @staticmethod
    def delete_course_by_id(course_id: str):
        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db)
                course_repository.delete_course_by_id(course_id)     
        except Exception as e:
            raise e
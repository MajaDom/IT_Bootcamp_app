from app.course.repository import CourseRepository
from app.db.database import SessionLocal
from app.course.exceptions import CourseNotFound, CourseExists

class CourseServices:
    @staticmethod
    def create_course(course_name, course_description):
        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db)
                c = course_repository.get_course_by_name(course_name)
                if c is None:
                    return course_repository.create_course(course_name, course_description)      
                raise CourseExists(message="Course already exists in the database.", code=400)
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

    @staticmethod
    def delete_course_by_id(course_id: str):
        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db)
                course_repository.delete_course_by_id(course_id)     
        except Exception as e:
            raise e

    @staticmethod
    def update_course(course_id: str, new_course: str):
        try:
            with SessionLocal() as db:
                course_repository = CourseRepository(db)                  
                return course_repository.update_course(course_id, new_course)          
        except Exception as e:
            raise e

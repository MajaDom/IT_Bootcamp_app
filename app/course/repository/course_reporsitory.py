from re import I
from sqlalchemy.exc import IntegrityError
from app.course.models import Course
from app.course.exceptions import CourseNotFound
from app.base.base_repository import BaseCRUDRepository
from app.base.base_exception import AppException

class CourseRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Course with this id is already registered.", code=400) from exc

    def get_course_by_id(self, course_id: str):
    
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if course is None:
            raise CourseNotFound(f"Course with provided ID: {course_id} not found.", 404)
        return course

    def get_course_by_name(self, course_name: str):
    
        course = self.db.query(Course).filter(Course.course_name == course_name).first()
        if course is None:
            raise CourseNotFound(f"Course with provided name: {course_name} not found.", 404)
        return course


    def get_all_courses(self):

        course = self.db.query(Course).all()
        return course



    # def update_course_name(self, course_id: str, new_name: str):

    #     try:
    #         course = self.db.query(Course).filter(Course.id == course_id).first()
    #         if course is None:
    #             raise CourseNotFound(f"Course with provided ID: {course_id} not found", 404) 
    #         course.course_name = new_name
    #         self.db.add(course)
    #         self.db.commit()
    #         self.db.refresh(course)
    #         return course
    #     except Exception as e:
    #         raise e
        
    def update_course_by_id(self, course_id, course_name, course_description):
            try:
                course = self.db.query(Course).filter(Course.id == course_id).first()
                course.course_name = course_name
                course.course_description = course_description
                self.db.add(course)
                self.db.commit()
                self.db.refresh(course)
                return course
            except IntegrityError as e:
                raise e
    

    def delete_course_by_id(self, course_id: str):

        try:
            course = self.db.query(Course).filter(Course.id == course_id).first()
            if course is None:
                raise  CourseNotFound(f"Course with provided ID: {course_id} not found", 404)
            self.db.delete(course)
            self.db.commit()
            return True
        except Exception as e:
            raise e
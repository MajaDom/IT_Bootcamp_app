from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.course.models import Course
from app.course.exceptions import CourseNotFound

class CourseRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_course(self, course_name, course_description): 

        try:
            course = Course(course_name, course_description)
            self.db.add(course)
            self.db.commit()
            self.db.refresh(course)
            return course
        except IntegrityError as e:
            raise e

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

    def update_course_name(self, course_id: str, new_name: str):

        try:
            course = self.db.query(Course).filter(Course.id == course_id).first()
            if course is None:
                raise CourseNotFound(f"Course with provided ID: {course_id} not found", 404) 
            course.course_name = new_name
            self.db.add(course)
            self.db.commit()
            self.db.refresh(course)
            return course
        except Exception as e:
            raise e
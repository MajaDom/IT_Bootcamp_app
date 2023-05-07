from app import course
from app.course.service import CourseServices
from app.course.exceptions import CourseNotFound, CourseExists
from fastapi import HTTPException, Response


class CourseController:

    @staticmethod
    def create_course(course_name, course_description):
        try:
            course = CourseServices.create_course(course_name, course_description)      
            return course

        except CourseExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_course_by_id(course_id: str):
        try:
            course = CourseServices.get_course_by_id(course_id) 
            if course:
                return course
        except CourseNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_course_by_name(course_name: str):
        try:
            course = CourseServices.get_course_by_id(course_name)
            if course:
                return course
        except CourseNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_courses():
        courses = CourseServices.get_all_courses()
        return courses
    
    


    # @staticmethod
    # def update_course_name(course_id: str, new_name: str):
    #     try:
    #         c = CourseServices.update_course_name(course_id, new_name)     
    #         return c
    #     except CourseNotFound as e:
    #         raise HTTPException(status_code=e.code, detail=e.message)
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=str(e))
        

    @staticmethod
    def update_course_by_id(course_id: str, course):
  
        try:
            CourseServices.update_course_by_id(course_id, course)        
            return Response(content=f"Course with id - {course_id} is updated")
        except CourseNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    @staticmethod
    def delete_course_by_id(course_id: str):
        try:
            CourseServices.delete_course_by_id(course_id)     
            return Response(content=f"Course with id - {course_id} is deleted")
        except CourseNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
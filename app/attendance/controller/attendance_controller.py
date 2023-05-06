from app.attendance.service import AttendanceServices
from app.attendance.exceptions import AttendanceNotFound, AttendanceExists
from fastapi import HTTPException, Response


class AttendanceController:

    @staticmethod
    def create_attendance(description, status, user_generation_id, lessons_id):
        try:
            attendance = AttendanceServices.create_attendance(description, status, user_generation_id, lessons_id)      
            return attendance

        except AttendanceExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_attendance_by_id(attendance_id: str):
        try:
            attendance = AttendanceServices.get_attendance_by_id(attendance_id) 
            if attendance:
                return attendance
        except AttendanceNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_all_attendances():
        attendances = AttendanceServices.get_all_attendances()
        return attendances
    

    @staticmethod
    def update_attendance_by_id(attendance_id: str, attendance):
  
        try:
            AttendanceServices.update_attendance_by_id(attendance_id, attendance)        
            return Response(content=f"Attendance with id - {attendance_id} is updated")
        except AttendanceNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    
    @staticmethod
    def delete_attendance_by_id(attendance_id: str):
        try:
            AttendanceServices.delete_attendance_by_id(attendance_id)     
            return Response(content=f"Attendance with id - {attendance_id} is deleted")
        except AttendanceNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



from app.db.database import SessionLocal
from app.attendance.repository import AttendanceRepository
from app.attendance.models import Attendance
from app.attendance.exceptions import AttendanceNotFound
from app.attendance.schemas import UpdateAttendanceSchemaIn
from fastapi.encoders import jsonable_encoder

class AttendanceServices:

    @staticmethod
    def create_attendance(status, description, user_generation_id, lessons_id):
        with SessionLocal() as db:
            try:
                attendance_repository = AttendanceRepository(db, Attendance)
                fields = {"status": status, "description": description, "user_generation_id": user_generation_id, "lessons_id": lessons_id}
                obj = attendance_repository.create(fields)
                return obj       
            except Exception as e:
                raise e


    @staticmethod
    def get_attendance_by_id(attendance_id: str):
        with SessionLocal() as db:
            try:
                attendance_repository = AttendanceRepository(db, Attendance)
                return attendance_repository.get_attendance_by_id(attendance_id)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_all_attendances():
        with SessionLocal() as db:
            attendance_repository = AttendanceRepository(db, Attendance)
            return attendance_repository.get_all_attendances()


    @staticmethod
    def update_attendance_by_id(attendance_id: str, attendance):
        try:
            with SessionLocal() as db:
                attendance_repository = AttendanceRepository(db, Attendance)
                stored_attendance_data = attendance_repository.get_attendance_by_id(
                    attendance_id)
                if not stored_attendance_data:
                    raise AttendanceNotFound(message="Attendance not found.", code=404)
                stored_attendance_model = UpdateAttendanceSchemaIn(
                    **jsonable_encoder(stored_attendance_data))
                update_data = attendance.dict(exclude_unset=True)
                updated_attendance = stored_attendance_model.copy(
                    update=update_data)
                return attendance_repository.update_attendance_by_id(attendance_id, updated_attendance.status, updated_attendance.description, updated_attendance.user_generation_id, updated_attendance.lessons_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_attendance_by_id(attendance_id: str):
        try:
            with SessionLocal() as db:
                attendance_repository = AttendanceRepository(db, Attendance)
                return attendance_repository.delete_attendance_by_id(attendance_id)
        except Exception as e:
            raise e




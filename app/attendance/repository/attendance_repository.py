from sqlalchemy.exc import IntegrityError
from app.attendance.models import Attendance
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException

class AttendanceRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Generation with this id is already registered.", code=400) from exc



    def get_attendance_by_id(self, attendance_id: str):
        attendance = self.db.query(Attendance).filter(Attendance.id == attendance_id).first()
        return attendance

    def get_all_attendances(self):
        attendances = self.db.query(Attendance).all()
        return attendances
    

    def update_attendance_by_id(self, attendance_id, status, description, user_generation_id, lessons_id):
            try:
                attendance = self.db.query(Attendance).filter(Attendance.id == attendance_id).first()
                attendance.status = status
                attendance.description = description
                attendance.user_generation_id = user_generation_id
                attendance.lessons_id = lessons_id
                self.db.add(attendance)
                self.db.commit()
                self.db.refresh(attendance)
                return attendance
            except IntegrityError as e:
                raise e


    def delete_attendance_by_id(self, attendance_id: str):
        try:
            attendance = self.db.query(Attendance).filter(Attendance.id == attendance_id).first()
            self.db.delete(attendance)
            self.db.commit()
            return True
        except Exception as e:
            raise e


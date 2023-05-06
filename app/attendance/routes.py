from fastapi import APIRouter
from app.attendance.controller import AttendanceController
from app.attendance.schemas import *

attendance_router = APIRouter(tags=["attendance"], prefix="/api/attendance")


@attendance_router.post("/add-new-attendance", response_model= AttendanceSchema)
def create_attendance(attendance: AttendanceSchemaIn):
    return AttendanceController.create_attendance(attendance.description, attendance.status, attendance.user_generation_id, attendance.lessons_id) 

@attendance_router.get("/id", response_model=AttendanceSchema)
def get_attendance_by_id(attendance_id: str):
    return AttendanceController.get_attendance_by_id(attendance_id)    

@attendance_router.get("/get-all-attendances", response_model=list[AttendanceSchema])
def get_all_attendances():
    return AttendanceController.get_all_attendances()

@attendance_router.patch("/update-attendances", response_model = AttendanceSchema) 
def update_attendance_by_id(attendance_id: str, attendance: UpdateAttendanceSchemaIn):
    return AttendanceController.update_attendance_by_id(attendance_id, attendance)

@attendance_router.delete("/")
def delete_attendance_by_id(attendance_id: str):
    return AttendanceController.delete_attendance_by_id(attendance_id)

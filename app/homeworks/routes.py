from fastapi import APIRouter, status
from app.homeworks.schemas import *
from app.homeworks.controller import HomeworkController

homework_router = APIRouter(prefix="/api/homeworks", tags=["Homeworks"])


@homework_router.post("/add-new-homework", response_model=HomeworkSchema, summary="Create Homework",
                      status_code=status.HTTP_201_CREATED)
def crate_homework(homework: HomeworkSchemaIn):
    """
    Function creates a new homework in the database.
    It takes as input a HomeworkSchemaIn object, which is validated and converted to an equivalent HomeworkSchema object.

    Param user:HomeworkSchemaIn: Tell the function that it will be receiving a homework object.
    Return: A dictionary with the homework's ID.
    """
    return HomeworkController.create_homework(homework.link, homework.description, homework.due_date, homework.file)


@homework_router.get("/all-homeworks", response_model=list[HomeworkSchema])
def read_all_homeworks():
    return HomeworkController.read_all()

from fastapi import APIRouter, status
from app.lessons.schemas import *
from app.lessons.controller import LessonController, MaterialController

lesson_router = APIRouter(prefix="/api/lessons", tags=["Lessons"])


@lesson_router.post("/add-new-lesson", response_model=LessonSchema, summary="Create Lesson",
                    status_code=status.HTTP_201_CREATED)
def crate_lesson(lesson: LessonSchemaIn):
    """
    Function creates a new lesson in the database.
    It takes as input a LessonSchemaIn object, which is validated and converted to an equivalent LessonSchemaOut object.

    Param user:LessonSchemaIn: Tell the function that it will be receiving a lesson object.
    Return: A dictionary with the lesson's ID.
    """
    return LessonController.create_lesson(lesson.lesson_title, lesson.description, lesson.content)


@lesson_router.get("/all-lessons", response_model=list[LessonSchema])
def read_all_lessons():
    return LessonController.read_all()


material_router = APIRouter(prefix="/api/materials", tags=["Materials"])


@material_router.post("/add-new-material", response_model=MaterialSchema, summary="Create Material",
                      status_code=status.HTTP_201_CREATED)
def crate_material(material: MaterialSchemaIn):
    return MaterialController.create_material(material.material_title, material.description, material.content,
                                              material.file)


@material_router.get("/all-materials", response_model=list[MaterialSchema])
def read_all_materials():
    return MaterialController.read_all()

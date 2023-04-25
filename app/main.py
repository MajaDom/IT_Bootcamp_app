import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.projects.routes import project_router
from app.users.routes import user_router
from app.course.routes import course_router
from app.generation.routes import generation_router
from app.consultations.routes import consultation_router
from app.lessons.routes import lesson_router


Base.metadata.create_all(bind=engine)


def init_app():
    app = FastAPI()
    app.include_router(user_router)
    app.include_router(course_router)
    app.include_router(consultation_router)
    app.include_router(generation_router)
    app.include_router(project_router)
    app.include_router(lesson_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == "__main__":
    uvicorn.run(app)

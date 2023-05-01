"""Material Service module"""


from app.lessons.exceptions.material_exceptions import MaterialDoesNotExistsException
from app.lessons.repositories import MaterialRepository
from app.db.database import SessionLocal
from app.lessons.models import Material


class MaterialService:
    """Service for Material routes."""

    @staticmethod
    def create_new_material(material_title: str, description: str, content: str, file: str):
        try:
            with SessionLocal() as db:
                repository = MaterialRepository(db, Material)
                fields = {
                    "material_title": material_title,
                    "description": description,
                    "content": content,
                    "file": file,
                }
                obj = repository.create(fields)
            return obj
        except Exception as exc:
            raise exc

    @staticmethod
    def read_all():
        try:
            with SessionLocal() as db:
                repository = MaterialRepository(db, Material)
                objs = repository.read_all()
                if not objs:
                    raise MaterialDoesNotExistsException(message=f"No materials in our Database.")
            return repository.read_all()
        except Exception as exc:
            raise exc

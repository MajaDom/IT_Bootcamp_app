"""Material Controller module"""
from fastapi import HTTPException


from app.base.base_exception import AppException
from app.lessons.service import MaterialService


class MaterialController:
    """Controller for Material routes"""
    @staticmethod
    def create_material(material_title: str, description: str, content: str, file: str):
        try:
            return MaterialService.create_new_material(material_title, description, content, file)
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

    @staticmethod
    def read_all():
        try:
            return MaterialService.read_all()
        except AppException as exc:
            raise HTTPException(status_code=exc.code, detail=exc.message) from exc
        except Exception as exc:
            raise HTTPException(status_code=500, detail=str(exc)) from exc

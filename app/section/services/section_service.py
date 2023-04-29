from app.db.database import SessionLocal
from app.section.repository import SectionRepository
from app.section.models import Section
from app.section.exceptions import SectionNotFound
from app.section.schemas import UpdateSectionSchemaIn
from fastapi.encoders import jsonable_encoder

class SectionServices:

    @staticmethod
    def create_section(section_title, start_date, end_date, generation_id):
        with SessionLocal() as db:
            try:
                section_repository = SectionRepository(db, Section)
                fields = {"section_title": section_title, "start_date": start_date, "end_date": end_date, "generation_id": generation_id}
                obj = section_repository.create(fields)
                return obj       
            except Exception as e:
                raise e

    @staticmethod
    def get_section_by_id(section_id: str):
        with SessionLocal() as db:
            try:
                section_repository = SectionRepository(db, Section)
                return section_repository.get_section_by_id(section_id)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_section_by_name(section_name: str):
        with SessionLocal() as db:
            try:
                section_repository = SectionRepository(db, Section)
                return section_repository.get_section_by_name(section_name=section_name)
            except Exception as e:
                raise e
            
    @staticmethod
    def get_section_by_name_partially(section_name: str):
        try:
            with SessionLocal() as db:
                repository = SectionRepository(db,Section)
                return repository.get_section_by_name_partially(section_name)
        except Exception as e:
            raise e


    @staticmethod
    def get_all_sections():
        with SessionLocal() as db:
            section_repository = SectionRepository(db, Section)
            return section_repository.get_all_sections()
        

    @staticmethod
    def update_section_title_by_id(section_id: str, new_section_title: str):
        try:
            with SessionLocal() as db:
                section_repository = SectionRepository(db, Section)                  
                return section_repository.update_section_title_by_id(section_id, new_section_title)          
        except Exception as e:
            raise e


    @staticmethod
    def update_section_by_id(section_id: str, section):
        try:
            with SessionLocal() as db:
                section_repository = SectionRepository(db, Section)
                stored_section_data = section_repository.get_section_by_id(
                    section_id)
                if not stored_section_data:
                    raise SectionNotFound(message="Section not found.", code=404)
                stored_section_model = UpdateSectionSchemaIn(
                    **jsonable_encoder(stored_section_data))
                update_data = section.dict(exclude_unset=True)
                updated_section = stored_section_model.copy(
                    update=update_data)
                return section_repository.update_section_by_id(section_id, updated_section.section_title, updated_section.start_date, updated_section.end_date, updated_section.generation_id)
        except Exception as e:
            raise e


    @staticmethod
    def delete_section_by_id(section_id: str):
        try:
            with SessionLocal() as db:
                section_repository = SectionRepository(db, Section)
                return section_repository.delete_section_by_id(section_id)
        except Exception as e:
            raise e

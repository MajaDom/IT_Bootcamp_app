from sqlalchemy.exc import IntegrityError
from app.base import BaseCRUDRepository
from app.base.base_exception import AppException
from app.section.models import Section
from app.section.exceptions import SectionNotFound

class SectionRepository(BaseCRUDRepository):

    def create(self, attributes: dict):
        try:
            return super().create(attributes)
        except IntegrityError as exc:
            self.db.rollback()
            raise AppException(message="Generation with this id is already registered.", code=400) from exc
        

    def get_section_by_id(self, section_id: str):
        section = self.db.query(Section).filter(Section.id == section_id).first()
        return section
    
    def get_section_by_name(self, section_name: str):

        section = self.db.query(Section).filter(Section.section_title == section_name).first()
        if section is None:
            raise SectionNotFound(f"Section with provided name: {section_name} not found.", 404)
        return section
    
    def get_section_by_name_partially(self, section_name: str):
        
        section = self.db.query(Section).filter(Section.section_title.ilike(f"%{section_name}%")).all()
        return section
        

    def get_all_sections(self):
        sections = self.db.query(Section).all()
        return sections
    
    
    def update_section_title_by_id(self, section_id: str, new_section_title: str):

        try:
            section = self.db.query(Section).filter(Section.id == section_id).first()
            if section is None:
                raise SectionNotFound(f"Section with provided ID: {section_id} not found", 404) 
            section.section_title = new_section_title
            self.db.add(section)
            self.db.commit()
            self.db.refresh(section)
            return section
        except Exception as e:
            raise e
        
    #TO DO: make update section by id, to update only certain attributess

    def delete_section_by_id(self, section_id: str):
        try:
            section = self.db.query(Section).filter(Section.id == section_id).first()
            self.db.delete(section)
            self.db.commit()
            return True
        except Exception as e:
            raise e



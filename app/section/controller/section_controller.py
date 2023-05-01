from app.section.services import SectionServices
from app.section.exceptions import SectionNotFound, SectionExists
from fastapi import HTTPException, Response


class SectionController:

    @staticmethod
    def create_section(section_title, start_date, end_date, generation_id):
        try:
            section = SectionServices.create_section(section_title, start_date, end_date, generation_id)      
            return section

        except SectionExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_section_by_id(section_id: str):
        try:
            section = SectionServices.get_section_by_id(section_id) 
            if section:
                return section
        except SectionNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_section_by_name(section_name: str):
        try:
            section = SectionServices.get_section_by_name(section_name)
            if section:
                return section
        except SectionNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    @staticmethod
    def get_section_by_name_partially(section_name: str):
        try:
            section = SectionServices.get_section_by_name_partially(section_name)
            return section
        except SectionNotFound as e:
            print(e)
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_sections():
        sections = SectionServices.get_all_sections()
        return sections

    @staticmethod
    def update_section_title_by_id(section_id: str, new_section_title: str):
        try:
            section = SectionServices.update_section_title_by_id(section_id, new_section_title)     
            return section
        except SectionNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        

    @staticmethod
    def update_section_by_id(section_id: str, section):
  
        try:
            SectionServices.update_section_by_id(section_id, section)        
            return Response(content=f"Section with id - {section_id} is updated")
        except SectionNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def delete_section_by_id(section_id: str):
        try:
            SectionServices.delete_section_by_id(section_id)     
            return Response(content=f"Section with id - {section_id} is deleted")
        except SectionNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))



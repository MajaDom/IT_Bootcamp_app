from fastapi import APIRouter, Depends
from app.section.controller import SectionController
from app.section.schemas import *

section_router = APIRouter(tags=["section"], prefix="/api/section")


@section_router.post("/add-new-section", response_model= SectionSchema)
def create_section(section: SectionSchemaIn):
    return SectionController.create_section(section.section_title, section.start_date, section.end_date, section.generation_id) 

@section_router.get("/id", response_model=SectionSchema)
def get_section_by_id(section_id: str):
    return SectionController.get_section_by_id(section_id)    

@section_router.get("/get-section_by_name", response_model=SectionSchema)
def get_section_by_name(section_name: str):
    return SectionController.get_section_by_name(section_name)  

@section_router.get("/get-section_by_name-partially", response_model=list[SectionSchema])
def get_section_by_name_partially(section_name: str):
    return SectionController.get_section_by_name_partially(section_name)

@section_router.get("/get-all-sections", response_model=list[SectionSchema])
def get_all_sections():
    return SectionController.get_all_sections()

@section_router.put("/update-section-title-by-id", response_model=SectionSchema)
def update_section_title_by_id(section_id, new_section_title):
    return SectionController.update_section_title_by_id(section_id, new_section_title)

@section_router.patch("/update-section", response_model = SectionSchema) 
def update_section_by_id(section_id: str, section: UpdateSectionSchemaIn):
    return SectionController.update_section_by_id(section_id, section)

@section_router.delete("/")
def delete_section_by_id(section_id: str):
    return SectionController.delete_section_by_id(section_id)
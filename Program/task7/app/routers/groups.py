from fastapi import APIRouter, HTTPException
from models import Group, Student, group_manager
from typing import List

router = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)

@router.get("/", response_model=List[Group])
def get_groups():
    """3.1. Возвращение списка групп на экран"""
    return group_manager.groups

@router.get("/{group_number}", response_model=Group)
def get_group_students(group_number: str):
    """3.2. Возвращение студентов группы"""
    group = group_manager.get_group(group_number)
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return group

@router.post("/{group_number}/add")
def add_student_to_group(group_number: str, student: Student):
    """3.3. Добавление студента в группу"""
    try:
        success = group_manager.add_student_to_group(group_number, student)
        if success:
            group_manager.save_to_file()  
            return {"message": f"Студент {student.name} добавлен в группу {group_number}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    raise HTTPException(status_code=500, detail="Ошибка при добавлении студента")

@router.delete("/{group_number}/delete/{student_number}")
def delete_student_from_group(group_number: str, student_number: int):
    """3.4. Удаление студента из группы по номеру в ведомости"""
    success = group_manager.remove_student_from_group(group_number, student_number)
    if success:
        group_manager.save_to_file()  
        return {"message": f"Студент с номером {student_number} удален из группы {group_number}"}
    else:
        raise HTTPException(status_code=404, detail="Группа или студент не найдены")

@router.put("")
def save_groups():
    """3.5. Сохранение групп в файл"""
    group_manager.save_to_file()
    return {"message": "Группы сохранены в файл"}

@router.post("")
def load_groups():
    """3.6. Загрузка групп из файла"""
    group_manager.load_from_file()
    return {"message": "Группы загружены из файла"}
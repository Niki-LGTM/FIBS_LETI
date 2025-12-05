# app/api/routes.py
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.core.repositories import (
    disciplines, enrollment, students,
    save_groups, save_students,
    save_disciplines, save_enrollments
)
from app.core.models import Discipline

router = APIRouter()
templates = Jinja2Templates(directory="app/presentation/templates")


# ====================== ДИСЦИПЛИНЫ ======================

@router.get("/disciplines", response_class=HTMLResponse)
async def list_disciplines(request: Request):
    return templates.TemplateResponse(
        "disciplines_list.html",
        {"request": request, "disciplines": sorted(disciplines.values(), key=lambda d: d.code)}
    )


@router.get("/disciplines/add", response_class=HTMLResponse)
async def add_discipline_form(request: Request):
    return templates.TemplateResponse("add_discipline.html", {"request": request})


@router.post("/disciplines/add")
async def add_discipline(code: str = Form(...), title: str = Form(...)):
    code = code.strip().upper()
    if code in disciplines:
        raise HTTPException(400, "Дисциплина с таким кодом уже существует")
    disciplines[code] = Discipline(code, title.strip())
    save_disciplines()
    return RedirectResponse("/disciplines", status_code=303)


@router.get("/disciplines/{code}", response_class=HTMLResponse)
async def discipline_detail(request: Request, code: str):
    disc = disciplines.get(code.upper())
    if not disc:
        raise HTTPException(404, "Дисциплина не найдена")
    return templates.TemplateResponse(
        "discipline_detail.html",
        {"request": request, "discipline": disc}
    )


@router.get("/disciplines/{code}/students", response_class=HTMLResponse)
async def discipline_students(request: Request, code: str):
    code = code.upper()
    disc = disciplines.get(code)
    if not disc:
        raise HTTPException(404, "Дисциплина не найдена")

    student_ids = enrollment.get_students(code)
    studs = [students[sid] for sid in student_ids if sid in students]
    return templates.TemplateResponse(
        "discipline_students.html",
        {"request": request, "discipline": disc, "students": studs}
    )


@router.get("/disciplines/{code}/add", response_class=HTMLResponse)
async def add_student_form(request: Request, code: str):
    code = code.upper()
    if code not in disciplines:
        raise HTTPException(404, "Дисциплина не найдена")

    already = enrollment.get_students(code)
    available = [s for s in students.values() if s.id not in already]

    return templates.TemplateResponse(
        "add_student.html",
        {"request": request, "discipline": disciplines[code], "students": available}
    )


@router.post("/disciplines/{code}/add")
async def add_student_post(code: str, student_id: int = Form(...)):
    code = code.upper()
    if code not in disciplines or student_id not in students:
        raise HTTPException(404, "Не найдено")
    enrollment.add(code, student_id)
    save_enrollments()
    return RedirectResponse(f"/disciplines/{code}/students", status_code=303)


# ====================== КНОПКИ СОХРАНЕНИЯ ======================

@router.post("/save/groups")
async def save_groups_api():
    save_groups()
    return {"status": "ok"}

@router.post("/save/students")
async def save_students_api():
    save_students()
    return {"status": "ok"}

@router.post("/save/disciplines")
async def save_disciplines_api():
    save_disciplines()
    return {"status": "ok"}

@router.post("/save/enrollments")
async def save_enrollments_api():
    save_enrollments()
    return {"status": "ok"}

# === ТЕСТОВЫЕ ДАННЫЕ ===
if not students:  
    from app.core.models import Student
    
    test_students = [
        Student(id=1, name="Иванов И.И.", group="ПМИ-21"),
        Student(id=2, name="Петров П.П.", group="ПМИ-21"),
        Student(id=3, name="Сидорова А.В.", group="ПМИ-22"),
        Student(id=4, name="Козлов Д.С.", group="ИВТ-21"),
        Student(id=5, name="Смирнова Е.А.", group="ПМИ-21"),
    ]
    
    for s in test_students:
        students[s.id] = s
    
    save_students()
    print("Добавлены тестовые студенты!")
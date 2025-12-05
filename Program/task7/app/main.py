from fastapi import FastAPI
from routers import users, groups
from models import group_manager

app = FastAPI(
    title="Student Groups Management API",
    description="Веб-приложение для управления группами студентов и пользователями",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(groups.router)

@app.on_event("startup")
async def startup_event():
    """Загружаем группы из файла при запуске приложения"""
    group_manager.load_from_file()

@app.get("/")
def root():
    return {
        "message": "Приложение работает!",
        "features": {
            "users": "Управление пользователями",
            "groups": "Управление группами студентов"
        },
        "endpoints": {
            "users": {
                "get_users": "GET /users/",
                "get_current_user": "GET /users/me"
            },
            "groups": {
                "get_groups": "GET /groups/",
                "get_group_students": "GET /groups/{group_number}",
                "add_student": "POST /groups/{group_number}/add",
                "delete_student": "DELETE /groups/{group_number}/delete/{student_number}",
                "save_groups": "PUT /groups",
                "load_groups": "POST /groups"
            }
        }
    }
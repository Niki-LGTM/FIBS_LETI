from fastapi import FastAPI
from app.api.routes import router
from app.core.repositories import load_all_data

app = FastAPI(title="ИДЗ-8 — Дисциплины")

app.include_router(router)
load_all_data()

@app.get("/")
async def root():
    return {"message": "ИДЗ-8 успешно запущен → перейдите на /disciplines"}
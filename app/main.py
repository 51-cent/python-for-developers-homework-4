from fastapi import FastAPI

from app.routes.form import router as form_router

app = FastAPI(title="Домашнее задание 4. FastAPI и Pydantic")

app.include_router(form_router, prefix="/form")

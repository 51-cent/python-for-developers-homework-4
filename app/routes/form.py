from fastapi import APIRouter, HTTPException

from app.shemas.form import FormRequest
from app.services.form import save_form

router = APIRouter()


@router.post("/send", tags=["send form"])
def form(request: FormRequest):
    if not save_form(request):
        raise HTTPException(status_code=500, detail="Не удалось сохранить обращение!")

    return {
        "success": True
    }

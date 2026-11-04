import json
import uuid
from pathlib import Path

from app.shemas.form import FormRequest

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'


def save_form(data: FormRequest) -> bool:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    form_id = str(uuid.uuid4())
    form_path = DATA_DIR / f"{form_id}.json"

    with form_path.open(mode="w", encoding="utf-8") as file:
        json.dump(data.model_dump(mode="json"), file, ensure_ascii=False, indent=4)

    return True

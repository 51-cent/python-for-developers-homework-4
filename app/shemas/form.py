import re
from datetime import date

from pydantic import BaseModel, Field, EmailStr, field_validator


class FormRequest(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    second_name: str = Field(min_length=2, max_length=50)
    birth_date: date
    phone: str
    email: EmailStr

    @field_validator('first_name', 'second_name')
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not re.fullmatch(r'[А-ЯЁ][а-яё]+', value):
            raise ValueError("Имя и фамилия должны начинаться с заглавной буквы и содержать только кириллицу")

        return value

    @field_validator('birth_date')
    @classmethod
    def validate_birth_date(cls, value: date) -> date:
        if value >= date.today():
            raise ValueError("Дата рождения должна быть в прошлом")

        return value

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, value: str) -> str:
        if not re.fullmatch(r"\+7\d{10}", value):
            raise ValueError("Телефон должен иметь формат +7XXXXXXXXXX")

        return value

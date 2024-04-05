from typing import Union, Optional
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class EmailCreate(BaseModel):
    email: str
    user_id: int

    class Config:
        schema_extra = {
            "example": {
                "email": "2050669795@qq.com",
                "user_id": 1
            }}

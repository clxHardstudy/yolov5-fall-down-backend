from pydantic import BaseModel
from typing import Union, List


class ImageIdentify(BaseModel):
    imagecontent: str

    class Config:
        schema_extra = {
            "example": {
                "imagecontent": "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"
            }}


class ImageRegister(ImageIdentify):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "李知恩",
                "imagecontent": "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"
            }}


class Image(BaseModel):
    name: str
    comment: str


class FallImage(BaseModel):
    filebase64str: str
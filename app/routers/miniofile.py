from concurrent.futures import ThreadPoolExecutor

from sqlalchemy.orm import Session
from app import crud, schemas, get_db
from fastapi import File, UploadFile, Depends
from fastapi import APIRouter
from typing import List

from app.core.storage.file import FMH

router_miniofile = APIRouter(
    prefix="/file",
    tags=["file-文件管理"],
)


@router_miniofile.post('/MinioFileBytes', summary="minio上传文件")
def upload_minio_file_bytes(item: schemas.FallImage, db: Session = Depends(get_db)):
    return crud.upload_minio_file_bytes(item=item, db=db)


@router_miniofile.post('/MinioFile', summary="minio上传文件")
def upload_minio_file(file: UploadFile = File(...)):
    return crud.upload_minio_file(file=file)


# 多个文件
@router_miniofile.post("/MinioFiles", summary="minio上传多个文件")
async def create_files(files: List[UploadFile] = File(...)):
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = executor.map(crud.upload_minio_file, files)
    uris = [result['uri'] for result in results]
    return {'uris': uris}


@router_miniofile.get("/{uri:path}/uri", summary="获取文件")
def get_minio_file(uri):
    print("获取文件")
    return crud.get_file(uri)


@router_miniofile.get("/fall_images", summary="获取图片地址")
def get_fall_images(db: Session = Depends(get_db)):
    print("获取文件地址")
    return crud.get_images_uri(db=db)

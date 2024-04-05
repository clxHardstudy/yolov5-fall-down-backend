import base64
import io
import os.path
import time

import cv2
import numpy as np
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app import schemas, models
from app.core.storage.file import MinioStorage

minio = MinioStorage()


def upload_minio_file_bytes(item: schemas.FallImage, db: Session):
    name = ".jpg"
    file_base64 = item.filebase64str
    # 解码 base64 图片数据为字节流
    image_bytes = base64.b64decode(file_base64)
    # 将字节流转换为图像
    img = cv2.imdecode(np.frombuffer(image_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
    # 编码图像为字节流
    img_bytes = cv2.imencode(".jpg", img)[1].tobytes()
    filename = str(int(time.time())) + name
    # 上传到 Minio
    uri = minio.upload_byte(file_byte=img_bytes, file_name=filename)
    db_item = models.Fallimage(**{
        'name': filename,
        "create_time": int(time.time()),
        "update_time": int(time.time()),
        "uri": uri
    })
    db.add(db_item)
    db.commit()
    db.flush()
    res = db_item.to_dict()
    print(res)
    return res


def upload_minio_file(file):
    return minio.upload(file)


def get_file(path: str):
    if 'minio' in path:
        return get_minio_file(path.split('minio/')[-1])
    else:
        raise Exception(404, f'path:{path},文件路径不合法，应包含"minio"')


def get_images_uri(db: Session):
    items = db.query(models.Fallimage).order_by(models.Fallimage.id.desc()).all()
    res = {"uri_list": []}
    if items:
        res.update({"status_code": 200})
    for item in items:
        print(item.uri)
        res["uri_list"].append(item.uri)
    print(res)
    return res


def get_minio_file(path: str):
    io_content, content_type = minio.get_content(path)
    # print(content_type)
    return StreamingResponse(io_content, media_type=content_type)


def get_minio_file_byte(path: str):
    if 'minio' in path:
        return minio.get_file_byte(path.split('minio/')[-1])
    else:
        raise Exception(404, f'path:{path},文件路径不合法，应包含"minio"')


def judge_mp4(file_path):
    size = os.path.getsize(file_path)
    headers = {
        "Accept-Ranges": "bytes",
        "Content-Length": str(size),
        "Content-Type": "video/mp4"
    }
    return headers

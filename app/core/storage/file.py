import io
import random
import time
from typing import Tuple
import magic
from pathlib import Path
from app.db.minio import FileHandler
from app.core.storage.base import FileStorage

FMH = FileHandler("falldetection")


class MinioStorage(FileStorage):
    def get_name(self, file_name) -> str:
        file_name = f'{time.strftime("%d%H%M%S", time.localtime())}{random.randint(1000, 9999)}{Path(file_name).suffix}'
        return file_name

    def get_uri(self, end_minio) -> str:
        uri = '/file/minio/' + end_minio
        return uri

    def upload(self, file):
        file_byte = file.file.read()
        file_name = self.get_name(file.filename)
        result = Path(time.strftime("%Y%m/%d", time.localtime()))
        real_path = result / file_name
        print(real_path)
        path = FMH.put_file(real_path, file_byte)
        uri = self.get_uri(path)
        return {'uri': uri}

    def upload_byte(self, file_byte, file_name) -> dict:
        result = Path(time.strftime("%Y%m/%d", time.localtime()))
        real_path = result / file_name
        path = FMH.put_file(real_path, file_byte)
        uri = self.get_uri(path)
        return uri

    def get_content(self, path) -> Tuple[io.BytesIO, str]:
        file_byte = FMH.get_file(path)
        content_type = magic.from_buffer(file_byte, mime=True)
        if file_byte:
            return io.BytesIO(file_byte), content_type
        else:
            raise Exception(404, f"文件 {path} 不存在")

    def get_file_byte(self, path):
        file_byte = FMH.get_file(path)
        if file_byte:
            return file_byte
        else:
            raise Exception(404, f"文件 {path} 不存在")

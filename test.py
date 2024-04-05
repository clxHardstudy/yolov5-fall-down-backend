import base64
import io
import os
from io import BytesIO

import cv2
import insightface
import numpy as np
from PIL import Image


# def Camera():
#     video_capture = cv2.VideoCapture(0)
#     if not video_capture.isOpened():
#         print("无法打开摄像头")
#         exit()
#     i = 0
#     while True:
#         i += 1
#         ret, frame = video_capture.read()
#         cv2.imshow('Camera', frame)
#         if i == 10:
#             cv2.imwrite("clx.jpg", frame)
#             video_capture.release()
#             cv2.destroyAllWindows()
# Camera()

# def base64_to_cv2(img: str):
#     # 注：仅适合图像，不适合其它numpy数组，例如bboxs(人脸标注框)的数据
#     # base64 -> 二进制 -> ndarray -> cv2
#     # 解码为二进制数据
#     img_codes = base64.b64decode(img)
#     img_np = np.frombuffer(img_codes, np.uint8)
#     img_cv2 = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
#     return img_cv2
#
import base64

# def image_to_base64(image_path):
#     with open(image_path, "rb") as image_file:
#         image_bytes = image_file.read()
#         base64_str = base64.b64encode(image_bytes).decode("utf-8")
#         return base64_str
#
# # 示例用法
# image_path = "/Users/clx/file/PycharmProjects/myself/final_project/下载.jpeg"
# base64_str = image_to_base64(image_path)
# print((base64_str))
# image_bytes = base64.b64decode(base64_str)
    # 将字节数据转换为图像
# image = Image.open(BytesIO(image_bytes))

# from sklearn import preprocessing
# faces_embedding = list()
# if not os.path.exists("face_db"):
#     os.makedirs("face_db")
# for root, dirs, files in os.walk("face_db"):
#     print(root,dirs,files)
#     for file in files:
#         print(file)
#         input_image = cv2.imdecode(np.fromfile(os.path.join(root, file), dtype=np.uint8), 1)
#         user_name = file.split(".")[0]
#         face = insightface.app.FaceAnalysis(root='./',
#                                                   allowed_modules=None,
#                                                   providers=['CUDAExecutionProvider']).get(input_image)[0]
#         embedding = np.array(face.embedding).reshape((1, -1))
#         embedding = preprocessing.normalize(embedding)
#         faces_embedding.append({
#             "user_name": user_name,
#             "feature": embedding
#         })
#         print(faces_embedding)

# print(os.path.exists("http://127.0.0.1:9000/minio/projectpractice/202307/"))


# from minio import Minio
#
# from app.core.storage.file import FMH
#
# # 创建MinIO客户端对象
# client = Minio(
#     endpoint="127.0.0.1:9000",
#     access_key="minioadmin",
#     secret_key="minioadmin",
#     secure=False  # 如果使用HTTPS连接，则设置为True，否则为False
# )
#
# # 列出存储桶中特定文件夹的所有文件
# bucket_name = "projectpractice"
# folder_name = "facestorage"
#
# objects = client.list_objects(bucket_name, prefix=folder_name, recursive=True)
#
# for obj in objects:
#     file_path = obj.object_name
#     FMH.minio_client.remove_object(bucket_name="projectpractice", object_name=file_path)
#     print("文件路径:", file_path)

# image_bytes = io.BytesIO(base64.b64decode("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"))
# image = Image.open(image_bytes)
# image.save("1111.jpg")
# # image = base64.b64decode("/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQEhUSEA8VFRUVFRUVFRUVFRUVFRUVFRUWFhUVFRUYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAQFSsdHR0tKy0tLS0tLS0rLS0rLSstLS0tMDctLS0tLS0tLSstLS0tLS0tNy0rLSstLS0tLTcrN//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAACAgMBAQAAAAAAAAAAAAABAgADBAYHBQj/xABEEAACAQIDBQQHBAYIBwAAAAAAAQIDEQQhMQUGEkFRE2FxkQciMoGhscFSctHwI0JiorLCFBYzNFNzkuEVNUNjs8Px/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAECAwT/xAAdEQEBAAIDAQEBAAAAAAAAAAAAAQIRAyExQRJR/9oADAMBAAIRAxEAPwDemxWFsVmmQYjCxWwAxWwsRsAMVkbFYAAQFwIAgACBguDiXUAguCUktchIVoy0kn4MCy5AEANw3FuQBrhTEuG4DhTEQUwHTGTK0x0wLEx0VJjoB7kEuQDMbFbI2K2AGxWyNitgBsVkYjYAkxWwsVsCMUjYGATwN5N68PgVab46j0pxa4vGX2UeVv7vY8LHsaD/AE0ldy/w4vn958vM5TBucryblJu7u3dvq3ncK3HE774zEO0eClHkld28Xz8jHp7fr0pXlN8Sd1LS/VvqeZQwsFFuTinys+Jr5lfDxNtyvZEHs7w7yV8SlZuKt7KyXe31PAwO3K9CalCTVnpnn1BKrK9o3sun1MmlgIVYu1Nxkvf/ALgdQ3W3soYyKjxqNW2cJZN98fte42E+dZxlCXNNO6ayaa0a6HTfR9vbKs/6NiZXnZunN6zS1i+slr4DY34lxbkKhiXFCA6ZELcNwGQ6ZWhkBYmOmVJjpgOQBAMtiMLFYAbEYWK2ArYjC2KwAxWFsVsCM8neXbMcHh51pK7WUI/am9F4c33JnqM5N6T9s9tXVCD9Wjfi6Oo9fJZeLYGo43FTrVJVKjvKbcpPvfTu5BwMVKcU1lcxz1NiYTjlfiatpbV9TKr8Yk21e1uWvyLcHhOODstB6+Hjnq88kvr3HobBwsp3UU7pc/kMlka5Up8Ms5OOfke3hcoX4lNpZJpqXulz8BNrYZxdpprw5nntzUbJ8UVyt6y71bl+IlSsLH4hVJX4bFeBxcqFSFWn7UJKS6Zcn3AxFNxbUtevXxMcDvuw9q08XRjWp6S1XOMllKL8DPucn9GG13SxDoSfq1U2u6pFXXmk17kdVuaiHuES4bgMEW4bgMmOmVoZMCxMZFaHTAa5AEAzGKwsVgKxGMxGwFYrYWIwI2KRgYGLtPFdjSqVLXcINpdWlkvOxwLHyvUm739Z3fV3zb8Xn7zt+9UrYWo+iTfhGSk/gjhUndu/UlIB6Oy5tXtq7JfU8893dTDdpVz0WfvM26ak3W27I2Q5RaWUnZeHE7L36v8A+m/7G3XhQodZNZsw93MHw8La19Z+/KK8rL3G7xfq2OW9vRqRoG393oVKTfD6y0fuv9Tnv/C+zm21ZaruT5fGx2/EWcJ5dH8Gc727h8p2WcV/PJXLMtM5Y7c227Ss13J593JPw0PIPe2rByV2tLeTy/A8KpGzZ0l242aW4DEulVhUX6k4y8mmd8wtZThGS/WSfmfPZ3HdKTeDoN6unH5GolewG4tyJlQ6YRQgMh0VpjoB0xkIhkAxCXIBmNiMZiMAMRhbEYCtisLFYAYrCwNhGLtOip0pxeacX8jie8WDw9OcP6M5uHBaXae12kZNTytpod0nKybONb21oyqqyVuFZr89TOXsbx8rW0jad0ZU6c12krX15vn+PxPGwmE4krJtt/n4fQ2DYjjGfD/R+1byUdF33fT8EZyax9dY2VtbCzlaFVaLJ5W5/gbPHERcbpo4vsXaOzsTNQlhp0pty9aE3JLhUbymrerF317npY3zZdF0HwKcpRtkmcr07zt7c6qUZ+MV8r/M1qjQjWdW+jio/v1XfycTK27jnRpNrVtv38Lt9PM0mNCrGHHUxqoRlo5S9qySVlq8kvMDwdvYTgnKL0zXzv8AVmo1F8MmbhtjCqV50sVGrJZ3T1/KNRqppyuvHuZ0xcM/VKVzveysOqVGnTWkIRj/AKUlc49ujs7+kYiMGrq8W30s+L5RkdqR0jFEKFIVDhFTGRQyGQiGQFiGQiGRA5BbkAzWKxmIwEYjHYjARisZiMIDYGRgYAksszi28OH4avZWzjk38jtJy7auE4sfVjJOzk9NbcK/38yWNRn7jbAVa0nfS1+l9UjocN1I01GVOK4l8V4mobi13SvB/qtryZ1TA17pHny9erHqTTVdmbr0qcqjjhYwdSMozktXGftJZtRvzskezT2YouKWdkld5vL6ntyatcxaFRSnZCm/5Gs7b2LPEV1CStSjbJaz0un3ZK/kePvPucq0VapKlUjPihUUW7LTgykmlzunrfqdHxrSmO6cZaovl6TqztyOe4cZQowpPOlHhlUtnO7u20tM27LOxrO+27DwsVJ87Rb775fU75VhCCyRyr0nYiNZxpXSSvOT6JZL4v4CW7SyfnqPC3F2f2VdOVrumpJLTPiVvvZN+9m/XNX3WhGtT7RZXeVsnHhyil7kbLTvbM7zx576cIoSoZDIRDIoZDIRDoB0xkxEMiIYgCAZzFYzEYUjEY8itgKxWMxWEKxbjMRgG5qO2cAli41HpUjbWy4krfSJthgbWwvaRXVO6/AK1fB/o68kubT5+/U6PsXEXijn2Npy4lUt7OUl0WSv5s2zYGKVlmcM5qvRx3cbknxI03+uMcLXVOtQnFZp1GvU4r6X/KPbq7boUV+lqxh95pfM8/8ArRsyu3CU4y72rxM7dJLfIvwu9NHG1nTpKTas0+FqL6tN6qxsCqNI83Z208HJ2oThe2iydvDoXYnErN3G0s11pg7f2moQbvyObSwLxHaVZe1UTjHuirNNd7yPT3s2h2lSNFS9qVn4czMwdNaW0tY6cc+uPJl8eVulh5UeOlLS6kvel9LGymFiMO1JVI6rJrrH8Vr59TKhNM6uRyACgGQRUMgHiOitDooYZCDIIa5AEIM9iSGEkFIxGPIrYAYrGFZUK2IxmKwFYGhmI2FU1aEWndaqz8DwtkYjsqrpN6aeHI9Pbe06eGoyq1Hklpzk3pFd7ZzfC7Xq1Z9vJ2k27JaKKdlE58k6b47qur7UwVOvSanTU3qrpNprpc0aUNn3ca1FRmnrFypv902ndreulK0arUX36G0ceEq5uNN+KTOFj14clx87c/2Ju7ha01OEakYR/WVSonJ9OK97Gwba2pGhTavyss8zL25tzCYeLScVbRR18EkafhsLWx8+1nFxgvZj9X3jTOedyu2kbV2pW7ZVllaT4Vydtb/I6Vu9tGniaSqQfc1zi7Zxf5zVmafvrsyNCnTjzcsvJtmvbF2rVwdTtKWfKcH7M49H39Hy80/Rhdx5c5quziqJibI2nSxVNVKUrp5Nc4vnGS5MzjTIECQAoZCIdFDRQ4qGQBCgIIQSEAB6EhJDSK5MKViMdiMgViDMVlQGKEACspxNeNOMpzkoxirtvJJIOMxVOlBzqzUYrVydkcj3v3pnjZcELxoxeUdHNr9af0XLxCsfe/eKWNqZXVKF+zj1/bl3v4ed/MweN4Ek+RjSjkVmLGo2OGPg1qXQxreUZv3NmrDRk1o35mfy1+m+7JwdJSVTE1YxXWpJLyu8z29pekXC4en2eEpurLTiacKa8/Wl5LxOUJDqI/E+n7vxn7Q2rWxdXtK83KXLkor7MVyRU0U0Fmy86RzpsPWqU3xUqkoPrGTi/hqexhd8sdTydVT7qkE/jGz+J4wkkEbphfSJNf2uGT74Ta/dkn8z2sHv1gp+2503+3F2843RzCxOEK7bgtoUayvRqwmv2ZJ28UtDMRwWKad02mtGsmvBo9rZ+9eOoWSrOa+zVXGv9XtfEDsVhkaJs/0iwaXb4eUX1puMl42k018Tc9n42nXgqlKalGWjXxTXJroUZKGFQUEGxCEAzmIx2IwpGIx2K0QVsDBia0KcXOclGKV3KTSSXe3oaTt70g0oXjhI9pL7crqmvBaz+C7yo3DE14U4uVSajFauTSS8WzS9t+kGnC8cLDtH9uV1BeC1l8DRdp7Vr4mXFXqufRaRj92KyRgzIMja+1q+KlxVqjlbRaRj92KyRg2DYEVdhpYksuK9udtc+aFxGGcHa6aavGS0lHk18rappp5oaSzHpzWklePdrF/aj35aaPyaDF4QqBkVKDiuJO8W7KS0v0a/Vfc/iIAFEspwbajFXbySJRoym1GEXKT0SV27K+ngrjzagmou7a9aS/hj3dXz8NSGUYr2W31btm7etw/s3vbu6aEFpLJDgRiVBmB6ABBSFuPEApA4R0BagV1tLG3+jDanBWlh5P1ai4o/fis7eMf4DT62o2zsY6FWFWOsJRl42ea96uveB31BK6FVTjGUXdSSkn1TV0/iWFRLACQDPYjHYjCkZ523NoLDUKlZq/BFtLrJ5RXvbS956LNL9KWJccNCC/6lWKfhGMpfNRA5ntDaNavOUq1WUm3dpt8N+Vo6JIxrEl7TCRAEY17gYFcg0FmBq5bSjlcKWaFLEhWgDTm46O18no010aeTXczJwlBVpxhGLU5yUYqK4otvubuvc34GKNSqyg1KLs1o0Bb2/CnGF43XDJ/rSXOLtpH9la828rY8ugW+YKftLzAvSDYjIgAwRCwIBGrOxdFCNXHAItMM5WQILIBZIxzIqckUSWbQHX/R5je1wUE3d03Km/CLvH91xNmOceibF+tXot8oVEvC8ZfyHRyiECQIzmIx2KwEZzT0s4n9Jh6d9I1JtfecYp/uyOls4/6Tqt8db7NKmvjOX8wVqeIdmn+cmWvMqxCul+dR6TyRELwtd4HmWgkgK+HkWSyXuBTWdyTCgtBJMIrQBIBEsBB6Mc2CMSyn9QHA0EjAXMih1CRAEICAVV2WRKZu7Ra3kAsc5eBXV9osoITELMDY/RxiODHRX+JCpD4cf8h2A4ludU4cdh3/ANy3+qLj9TtpRCEIEZ7EY7FZFIzivpF/5hV8Kf8A44namcZ9JEbY+p3xpv8AcS+hRrNT2fevmSg8mujK5yyY1J5te8gtAyNhgrvwAZRsiuoy1lFTVAGwbDJEaAVoFhyWAkVzDDQk9BwIAjIBLEIQCMWbCiubAphnIuqaFFL2i+eoU9PQSuiyKFqBFuwavDiaEulal/GrnekfOyk4u6dmndPo1mmfQ9KfFFNc0n55gpiBIVGexGOxGRSs4v6RZXx9XujTX7if1O0KLemZoW3PRvjsZi6tbipU6c5Rs5yblaMIxvwRT+zzaFsiyWuVV0CzXDJppO9nZ2dsnZ8ztezPRFhadpYmvOs1m4xSp033NZya96Ns2vuvgMXSp0q9NdnS9iMZOmo5WsuBo53ONzjunzfJlsI2R2jGejbZMsocdN8pQqyk/KfEvgcm29go4bEVaEaiqKnPhU1lxKyel9Vez70zUylZywuPrAZjvUukylM0yuSCCLDcAEI2elsTB0asl21Rxhd8fDfijCMeJyVoyfK3svlk7kt0rzSwWTjxPhvw3duK3Fa+V7ZXtYYqAAjIBASGEbADZXIdsrbAFPVli1Kqcs2XU0BYhZDAYGJWWZ3zYFXjw1CX2qNN+cInBq6O47nyvgsP/kwXkrfQD1wkCBlsRhIUZOz9T2auhCHDL2u+HkYeL9lmhby+yyEOWXrtj403Ff2bNIoaIhDtxfXDm+Gq6FUSEOrktgOQgQJfnyNq9HH94f3Kv/oCQlWNWfte6P8ACgshCzxAZEQgEK/xfzIQBYlc9QkASjzMhEIA7IEgFFc7ZuR/ccP/AJa+pCAe4QhAP//Z")
# # print(image)

import time

# 获得当前时间时间戳
now = int(time.time())
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)
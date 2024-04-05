from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


class Fallimage(BaseModel):
    __tablename__ = "fallimage"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='图片名', unique=True)
    create_time = Column(Integer, comment='创建时间')
    update_time = Column(Integer, comment='更新时间')
    uri = Column(String(255), comment="图片地址")

from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


class EmailCode(BaseModel):
    __tablename__ = "emailcode"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    email = Column(String(255), comment='邮箱')
    valid_code = Column(String(255), comment="验证码")
    create_time = Column(Integer, comment='创建时间')
    user_id = Column(Integer, comment="用户id")

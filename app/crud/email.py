import time
from app import models, schemas, get_db
from sqlalchemy.orm import Session
from sendEmail import send_email


def create_email(db: Session, item: schemas.EmailCreate):
    validcode = send_email(item.email)
    db_item = models.EmailCode(**{
        'email': item.email,
        'valid_code': validcode,
        "create_time": int(time.time()),
        "user_id": item.user_id,
    })
    db.add(db_item)
    db.commit()
    db.flush()
    res = db_item.to_dict()
    print(res)
    return res


def bind_email(db: Session, items: schemas.EmailCreate):
    user = db.query(models.User).filter(models.User.id == items.user_id).first()
    if user:
        user.email = items.email
    db.commit()
    db.flush()
    res = user.to_dict()
    print(res)
    print("邮箱绑定成功！")
    return res

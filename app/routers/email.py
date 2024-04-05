from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app import get_db, models

router_email = APIRouter(
    prefix="/email",
    tags=["email-邮箱"],
)


@router_email.post("", summary="发送邮件")
def send_email_interface(item: schemas.EmailCreate, db: Session = Depends(get_db)):
    return crud.create_email(db=db, item=item)


@router_email.put("/bind", summary="绑定邮箱")
def bind_email_user(items: schemas.EmailCreate, db: Session = Depends(get_db)):
    return crud.bind_email(db=db, items=items)

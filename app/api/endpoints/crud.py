from sqlalchemy.orm import Session
from . import schemas  
from . import models   

# Функция для аутентификации пользователя
def authenticate_user(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.username == username, models.User.password == password).first()

# Функция для создания нового запроса владельцем
def create_owner_request(db: Session, request: schemas.RequestCreate):
    db_request = models.Request(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Функция для редактирования запроса владельцем
def edit_owner_request(db: Session, request_id: int, request: schemas.RequestEdit):
    db_request = db.query(models.Request).filter(models.Request.id == request_id).first()
    if db_request:
        for field, value in request.dict().items():
            setattr(db_request, field, value)
        db.commit()
        db.refresh(db_request)
    return db_request

# Функция для получения всех сотрудников
def get_all_employees(db: Session):
    return db.query(models.Employee).all()



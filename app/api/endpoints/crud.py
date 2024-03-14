from sqlalchemy.orm import Session
from . import schemas  
from app.api import models   

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

# Функция для получения запросов на рассмотрении владельцем
def get_owner_pending_requests(db: Session):
    considered_requests = db.query(models.Request).filter(
        models.Request.status == 'не_рассмотрен', #заменить на нужные
        models.Request.user_type == 'владелец' #заменить на нужные
    ).all()
    return considered_requests


# Функция для получения расмотренных запросов для владельцы
def get_owner_reviewed_requests(db: Session):
    considered_requests = db.query(models.Request).filter(
        models.Request.status == 'рассмотрен', #заменить на нужные
        models.Request.user_type == 'владелец' #заменить на нужные
    ).all()
    return considered_requests

# Функция для получения всех сотрудников
def get_all_employees(db: Session):
    return db.query(models.Employee).all()

# Функция для получения расмотренных запросов для администратора
def get_admin_review_request(db: Session):
    db_requests = db.query(models.Request).filter_by(status='considered').all()
    return db_requests

# Функция для создания нового запроса админом
def create_admin_request(db: Session, request: schemas.RequestCreate):
    db_request = models.Request(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Функция для получения расмотренных запросов для администратора
def get_admin_pending_requests(db: Session):
    considered_requests = db.query(models.Request).filter(
        models.Request.status == 'не_рассмотрен', #заменить на нужные
        models.Request.user_type == 'администратор' #заменить на нужные
    ).all()
    return considered_requests

# Функция для просмотра личного кабинета владельца
def get_owner_profile(db: Session, owner_id: int): # Эндпоинт для просмотра личного кабинета владельца - добавить параметр owner_id в функцию
    # Получаем данные о владельце по его идентификатору
    owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()
    return owner

#
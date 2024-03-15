from sqlalchemy.orm import Session
from . import schemas  
from app.api.models import employee   
from app.api.models import request as request_model

# Функция для аутентификации пользователя
def authenticate_user(db: Session, username: str, password: str):
    return db.query(employee.User).filter(employee.User.Логин == username, employee.User.Пароль == password).first()

# Функция для создания нового запроса владельцем - не работает, выходные данные очень странные
def create_owner_request(db: Session, request: schemas.RequestCreate):
    db_request = request_model.Request(**request.dict())
    print(db_request)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Функция для редактирования запроса владельцем - не работает, выходные данные очень странные
def edit_owner_request(db: Session, request_id: int, request: schemas.RequestEdit):
    db_request = db.query(request.Request).filter(request.Request.id == request_id).first()
    if db_request:
        for field, value in request.dict().items():
            setattr(db_request, field, value)
        db.commit()
        db.refresh(db_request)
    return db_request

# Функция для получения запросов на рассмотрении владельцем
def get_owner_pending_requests(db: Session):
    considered_requests = db.query(request_model.Request).filter(
        request_model.Request.Статус == 'В обработке', #заменить на нужные
        employee.User.Роль_на_сайте == 'dir' #заменить на нужные
    ).all()
    print("Получено запросов:", len(considered_requests))
    return considered_requests


# Функция для получения расмотренных запросов для владельцы
def get_owner_reviewed_requests(db: Session):
    considered_requests = db.query(request_model.Request).filter(
        request_model.Request.Статус == 'рассмотрен', #заменить на нужные
        employee.User.Роль_на_сайте == 'владелец' #заменить на нужные
    ).all()
    return considered_requests

# Функция для получения всех сотрудников
def get_all_employees(db: Session):
    return db.query(employee.Employee).all()

# Функция для получения расмотренных запросов для администратора
def get_admin_review_request(db: Session):
    db_requests = db.query(request_model.Request).filter_by(status='considered').all()
    return db_requests

# Функция для создания нового запроса админом
def create_admin_request(db: Session, request: schemas.RequestCreate):
    db_request = request_model.Request(**request.dict())
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Функция для получения расмотренных запросов для администратора
def get_admin_pending_requests(db: Session):
    considered_requests = db.query(request_model.Request).filter(
        request_model.Request.status == 'не_рассмотрен', #заменить на нужные
        request_model.Request.user_type == 'администратор' #заменить на нужные
    ).all()
    return considered_requests

'''
# Функция для просмотра личного кабинета владельца
def get_owner_profile(db: Session, owner_id: int): # Эндпоинт для просмотра личного кабинета владельца - добавить параметр owner_id в функцию
    # Получаем данные о владельце по его идентификатору
    owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()
    return owner
'''
#
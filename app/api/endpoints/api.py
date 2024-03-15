from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.endpoints import crud, schemas
from app.db.base_class import get_db


router = APIRouter()


# Эндпоинт для аутентификации пользователей
@router.post("/login/")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": crud.create_access_token(data={"sub": user.username})}


# Эндпоинт для просмотра запросов на рассмотрении владельцем
@router.get("/owner/requests/pending", response_model=list[schemas.Request])
def get_owner_pending_requests(db: Session = Depends(get_db)):
    return crud.get_owner_pending_requests(db=db)


# Эндпоинт для просмотра рассмотренных запросов владельцем
@router.get("/owner/requests/reviewed", response_model=list[schemas.Request])
def get_owner_reviewed_requests(db: Session = Depends(get_db)):
    return crud.get_owner_reviewed_requests(db=db)


# Эндпоинт для создания нового запроса владельцем
@router.post("/owner/requests/", response_model=schemas.Request)
def create_owner_request(request: schemas.RequestCreate, db: Session = Depends(get_db)):
    return crud.create_owner_request(db=db, request=request)


# Эндпоинт для редактирования запроса владельцем
@router.put("/owner/requests/{request_id}/", response_model=schemas.Request)
def edit_owner_request(
    request_id: int, request: schemas.RequestEdit, db: Session = Depends(get_db)
):
    return crud.edit_owner_request(db=db, request_id=request_id, request=request)


# Эндпоинт для просмотра личного кабинета владельца
@router.get("/owner/profile", response_model=schemas.OwnerProfile)
def get_owner_profile(db: Session = Depends(get_db)):
    return crud.get_owner_profile(db=db)


# Эндпоинт для получения расмотренных запросов для администратора
@router.get("/admin/request/reviewed", response_model=list[schemas.Request])
def get_admin_review_request(db: Session = Depends(get_db)):
    return crud.get_admin_review_request(db=db)


# Эндпоинт для получения запросов на рассмотрении
@router.get("/admin/requests/pending", response_model=list[schemas.Request])
def get_admin_pending_requests(db: Session = Depends(get_db)):
    return crud.get_admin_pending_requests(db=db)


# Эндопоинт для создания нового запроса админом
@router.post("/admin/requests/", response_model=schemas.Request)
def create_admin_request(request: schemas.RequestCreate, db: Session = Depends(get_db)):
    return crud.create_admin_request(db=db, request=request)


# Эндпоинт для редактирования запроса
@router.put("/admin/requests/{request_iq}", response_model=schemas.Request)
def edit_admin_request(
    request_id: int, request: schemas.RequestEdit, db: Session = Depends(get_db)
):
    return crud.edit_admin_request(db=db, request_id=request_id, request=request)


# Эндпоинт для добавления новых пользователей в базу данных
@router.post("/admin/employees/create", response_model=schemas.Employee)
def admin_create_employees(
    employeer: schemas.EmployeeCreate, db: Session = Depends(get_db)
):
    # Проверка не зарегестрировался ли еще пользаватель
    existing_employeer = crud.get_employeer_by_employee_id(
        db, employee_id=employeer.employee_id
    )
    if existing_employeer:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    # Создаем нового пользователя
    return crud.create_user(db=db, employeer=employeer)


# Эндпоинт для графикто это пиздец пока не будем делать


# Эндпоинт для создания нового запроса
@router.post("/employee/requests/", response_model=schemas.Request)
def create_employee_request(
    request: schemas.RequestCreate, db: Session = Depends(get_db)
):
    return crud.create_employee_request(db=db, request=request)


# Эндпоинт для получения всех рассмотреных запросов.
@router.get("/employee/requests/reviewed", response_model=list[schemas.Request])
def get_employee_reviwed_request(db: Session = Depends(get_db)):
    return crud.get_employee_reviwed_request(db=db)


# Эндпоинт для получения запросов на рассмотрении.
@router.get("/employee/requests/pending", response_model=list[schemas.Request])
def get_employee_pending_request(db: Session = Depends(get_db)):
    return crud.get_employee_pending_request(db=db)


# Эндпоинт для просмотра всех сотрудников из базы данных
@router.get("/admin/employees", response_model=list[schemas.Employee])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_all_employees(db=db)

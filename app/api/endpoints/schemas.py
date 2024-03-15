from pydantic import BaseModel
from typing import Optional, List


# Схема данных для запроса аутентификации пользователя
class LoginRequest(BaseModel):
    username: str
    password: str


class Request(BaseModel):
    topic: str
    labels: str
    description: str
    request_date: Optional[str] = None
    response_date: Optional[str] = None
    status: Optional[str] = None
    employee_id: int


# Схема данных для создания нового запроса
class RequestCreate(BaseModel):
    topic: str
    labels: str
    description: str
    request_date: Optional[str] = None
    response_date: Optional[str] = None
    status: Optional[str] = None
    employee_id: int


# Схема данных для редактирования запроса
class RequestEdit(BaseModel):
    topic: Optional[str] = None
    labels: Optional[str] = None
    description: Optional[str] = None
    request_date: Optional[str] = None
    response_date: Optional[str] = None
    status: Optional[str] = None
    employee_id: Optional[int] = None


# Схема данных для профиля владельца
class OwnerProfile(BaseModel):
    owner_id: int
    username: str
    email: str


# Схема данных для сотрудника
class Employee(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    position: str
    role: str


# Cхема данных для создания сотрудника
class EmployeeCreate(BaseModel):
    password: str
    email: str
    first_name: str
    last_name: str
    position: str
    role: str



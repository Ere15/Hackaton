from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(Base):
    __tablename__ = "сотрудники"

    id_сотрудника = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True, nullable=False)
    Фамилия = Column(String, nullable=False)
    Имя = Column(String, nullable=False)
    Должность = Column(String, nullable=False)
    Логин = Column(String, unique=True, index=True, nullable=False)
    Пароль = Column(String, nullable=False)
    Роль_на_сайте = Column(String, nullable=False)

    # Определение обратного отношения один-ко-многим с таблицей "Запросы"
    запросы = relationship("Request", back_populates="сотрудник")  # Переименовал "Запросы" в "Requests"


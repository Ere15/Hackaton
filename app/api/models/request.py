from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Запросы(Base):
    __tablename__ = "Запросы"

    id_запроса = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True, nullable=False)
    Тема = Column(String, nullable=False)
    Метки = Column(String, nullable=False)
    Описание = Column(String, nullable=False)
    Дата_запроса = Column(Date, nullable=False)
    Дата_ответа = Column(Date)
    Статус = Column(String, nullable=False)
    id_сотрудника = Column(Integer,  ForeignKey('Сотрудники.id'), nullable=False)

    # Определение отношения один-ко-многим с таблицей "Сотрудники"
    Сотрудники = relationship("Сотрудники", back_populates="Запросы")

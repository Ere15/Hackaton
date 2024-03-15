from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class Request(Base):
    __tablename__ = "запросы"

    id_запроса = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True, nullable=False)
    Тема = Column(String, nullable=False)
    Метки = Column(String, nullable=False)
    Описание = Column(String, nullable=False)
    Дата_запроса = Column(Date, nullable=False)
    Дата_ответа = Column(Date)
    Статус = Column(String, nullable=False)
    id_сотрудника = Column(Integer, ForeignKey('сотрудники.id_сотрудника'), nullable=False)

    # Определение отношения многие-ко-одному с таблицей "Сотрудники"
    сотрудник = relationship("User", back_populates="запросы")  # Переименовал "Сотрудники" в "User"

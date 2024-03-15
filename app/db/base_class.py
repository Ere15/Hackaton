from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sqlite3
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение строки подключения к базе данных из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL")
    
# Создание экземпляра базового класса дляЫ всех моделей данных
Base = declarative_base()

engine = create_engine(DATABASE_URL)

# Создание соединения с базой данных
# engine = create_engine('sqlite:///hakatonDB.db', echo=True)

# Создание сессии SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# подключение к базе данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
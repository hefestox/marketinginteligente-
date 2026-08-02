from sqlalchemy import Boolean, Column, Integer, String
from app.database.connection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    idade = Column(Integer, nullable=True)
    sexo = Column(String, nullable=True)
    cidade = Column(String, nullable=True)
    aceitou_lgpd = Column(Boolean, default=False, nullable=False)

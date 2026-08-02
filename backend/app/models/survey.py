from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)

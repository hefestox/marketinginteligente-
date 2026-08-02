from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(180), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    idade = Column(Integer, nullable=True)
    sexo = Column(String(30), nullable=True)
    cidade = Column(String(120), nullable=True)
    aceitou_lgpd = Column(Boolean, default=False, nullable=False)

    rewards = relationship("Reward", back_populates="user")
    answers = relationship("Answer", back_populates="user")


class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(180), nullable=False)
    descricao = Column(Text, nullable=True)

    answers = relationship("Answer", back_populates="survey")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    resposta = Column(Text, nullable=False)

    user = relationship("User", back_populates="answers")
    survey = relationship("Survey", back_populates="answers")


class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pontos = Column(Integer, default=0, nullable=False)
    saldo = Column(Float, default=0.0, nullable=False)
    historico = Column(Text, nullable=True)

    user = relationship("User", back_populates="rewards")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(180), nullable=False)
    email = Column(String(180), unique=True, nullable=False)

    campaigns = relationship("Campaign", back_populates="company")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    titulo = Column(String(180), nullable=False)
    orcamento = Column(Float, default=0.0, nullable=False)

    company = relationship("Company", back_populates="campaigns")

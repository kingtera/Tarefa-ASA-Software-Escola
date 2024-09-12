from sqlalchemy import String, Integer, Column, ForeignKey
from .database import Base

class Cursos(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(45), nullable=False)
    professor_idProfessor = Column(Integer, ForeignKey('professores.id'))
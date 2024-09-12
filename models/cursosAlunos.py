from sqlalchemy import String, Integer, Column, text, ForeignKey
from .database import Base

class CursosAlunos(Base):
    __tablename__ = 'cursos_alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    curso_idCurso = Column(Integer, ForeignKey('cursos.id'))
    aluno_idAluno = Column(Integer, ForeignKey('alunos.id'))
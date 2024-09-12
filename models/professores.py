from sqlalchemy import String, Integer, Column
from .database import Base

class Professores(Base):
    __tablename__ = 'professores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(45), nullable=False)
    cpf = Column(Integer, server_default="0")
    cidade = Column(String(45))
    estado = Column(String(45))
    endereco = Column(String(50))
    numero = Column(Integer, server_default="0")
    complemento = Column(String(45))
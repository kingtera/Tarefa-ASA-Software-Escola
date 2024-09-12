from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    email: str
    cpf: int
    cidade: str
    estado: str
    endereco: str
    numero: int
    complemento: str
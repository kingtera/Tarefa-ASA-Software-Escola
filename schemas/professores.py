from pydantic import BaseModel

class Professor(BaseModel):
    nome: str
    email: str
    cpf: int
    cidade: str
    estado: str
    endereco: str
    numero: int
    complemento: str
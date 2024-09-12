from pydantic import BaseModel

class Curso(BaseModel):
    nome: str
    professor_idProfessor: int
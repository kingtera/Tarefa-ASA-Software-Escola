from pydantic import BaseModel

class Curso_Aluno(BaseModel):
    curso_idCurso: int
    aluno_idAluno: int
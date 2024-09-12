from fastapi import FastAPI
from typing import Optional
from routers.alunos import router as router_alunos
from routers.cursos import router as router_cursos
from routers.professores import router as router_professores
from routers.cursosAlunos import router as router_cursosAlunos
from models.database import engine
from models.alunos import Alunos
from models.alunos import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_alunos)
app.include_router(router_cursos)
app.include_router(router_professores)
app.include_router(router_cursosAlunos)
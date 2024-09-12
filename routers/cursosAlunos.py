from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.cursosAlunos   import Curso_Aluno
from models.database  import get_db
from models.cursosAlunos    import CursosAlunos
from sqlalchemy.orm   import Session
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

router = APIRouter()

@router.get("/cursosAlunos")
def get(db: Session = Depends(get_db)):
    all_cursosAlunos = db.query(CursosAlunos).all()
    return all_cursosAlunos


@router.post("/cursosAlunos")
async def criar_cursosAlunos(curso: Curso_Aluno, db: Session = Depends(get_db)):
    nova_Curso = CursosAlunos(**curso.model_dump())
    try:
        db.add(nova_Curso)
        db.commit()
        db.refresh(nova_Curso)
        return { "mensagem": "Curso_Aluno criado com sucesso",
                 "nova_Curso": nova_Curso}
    except Exception as e:
            print(e)
            return { "mensagem": "Problemas para inserir o curso",
                 "nova_Curso": nova_Curso}

 
@router.delete("/cursosAlunos/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(CursosAlunos).filter(CursosAlunos.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso_Aluno não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


@router.put("/cursosAlunos/{id}")
def update(id: int, curso:Curso_Aluno, db:Session = Depends(get_db)):
    updated_post = db.query(CursosAlunos).filter(CursosAlunos.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso_Aluno: {id} does not exist')
    else:
        updated_post.update(curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()
from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.cursos   import Curso
from models.database  import get_db
from models.cursos    import Cursos
from sqlalchemy.orm   import Session
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

router = APIRouter()

@router.get("/cursos")
def get(db: Session = Depends(get_db)):
    all_Cursos = db.query(Cursos).all()
    return all_Cursos


@router.post("/cursos")
async def criar_cursos(Curso: Curso, db: Session = Depends(get_db)):
    nova_Curso = Cursos(**Curso.model_dump())
    try:
        db.add(nova_Curso)
        db.commit()
        db.refresh(nova_Curso)
        return { "mensagem": "Curso criado com sucesso",
                 "nova_Curso": nova_Curso}
    except Exception as e:
            print(e)
            return { "mensagem": "Problemas para inserir o curso",
                 "nova_Curso": nova_Curso}

 
@router.delete("/cursos/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Cursos).filter(Cursos.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


@router.put("/cursos/{id}")
def update(id: int, Curso:Curso, db:Session = Depends(get_db)):
    updated_post = db.query(Cursos).filter(Cursos.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso: {id} does not exist')
    else:
        updated_post.update(Curso.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()
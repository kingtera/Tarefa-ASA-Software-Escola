from fastapi          import APIRouter, Depends, HTTPException, Response, status
from schemas.professores   import Professor
from models.database  import get_db
from models.professores    import Professores
from sqlalchemy.orm   import Session
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

router = APIRouter()

@router.get("/professores")
def get(db: Session = Depends(get_db)):
    all_professores = db.query(Professores).all()
    logging.info("GET_ALL_PROFESSORES")
    professores = []
    for professor in all_professores:
        item = {"id": professor.id,
                "nome": professor.nome}
        professores.append(item)       
    logging.info(professores)
    return all_professores


@router.post("/professores")
async def criar_professores(professor: Professor, db: Session = Depends(get_db)):
    novo_professor = Professores(**professor.model_dump())
    try:
        db.add(novo_professor)
        db.commit()
        db.refresh(novo_professor)
        logging.info("Professor criado com sucesso")
        return { "mensagem": "Professor criado com sucesso",
                 "novo_professor": novo_professor}
    except Exception as e:
            logging.error(e)
            return { "mensagem": "Problemas para inserir o Professor",
                 "novo_professor": novo_professor}

 
@router.delete("/professores/{id}")
def delete(id:int ,db: Session = Depends(get_db), status_code = status.HTTP_204_NO_CONTENT):
    delete_post = db.query(Professores).filter(Professores.id == id)
    
    if delete_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Professor não existe")
    else:
        delete_post.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)   


@router.put("/professores/{id}")
def update(id: int, professor: Professor, db:Session = Depends(get_db)):
    updated_post = db.query(Professores).filter(Professores.id == id)
    updated_post.first()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Professor: {id} does not exist')
    else:
        updated_post.update(professor.model_dump(), synchronize_session=False)
        db.commit()
    return updated_post.first()
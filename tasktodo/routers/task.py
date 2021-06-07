from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from tasktodo import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from tasktodo.repository import task

router = APIRouter(
    prefix="/task",
    tags=['Task']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.ShowTask])
def get_all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return models.Task.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Task, db: Session = Depends(get_db),
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return models.Task.create(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db),  
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return models.Task.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Task, db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return models.Task.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowTask)
def show(id:int, db: Session = Depends(get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return models.Task.show(id,db)
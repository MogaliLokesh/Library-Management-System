from fastapi import FastAPI,Depends,status,Response,APIRouter
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..essential import user


router = APIRouter(
    prefix = "/user",
)
get_db=database.get_db

@router.post('/')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
   
    return user.create_user(request,db)

@router.get('/{name}',status_code=200)
def get_user(name,response:Response,db:Session=Depends(get_db)):
    return user.get_user(name,response,db)

@router.put('/{name}/issue_book')
def issue_book(name,book_id:int,response:Response,db:Session=Depends(get_db),):
    return  user.issue_book(name,book_id,response,db)


@router.put('/{name}/return_book')
def return_book(name,book_id:int,response:Response,db:Session=Depends(get_db),):
    return  user.return_book(name,book_id,response,db)
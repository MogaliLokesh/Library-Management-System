
from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database
from sqlalchemy.orm import Session
from ..essential import book

router = APIRouter(
    prefix = "/book",
)

get_db=database.get_db

@router.post('/book',status_code=201)
def create_book(request: schemas.Book,db:Session=Depends(get_db)):
   return book.create_book(request,db)

@router.get('/book')
def get_all_books(db:Session=Depends(get_db)):
    return book.get_all_books(db)


@router.get('/book/{id}',status_code=200)
def get_book(id,response:Response,db:Session=Depends(get_db)):
    return book.get_book(id,response,db)
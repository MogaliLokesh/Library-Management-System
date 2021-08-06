
from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database
from sqlalchemy.orm import Session
from ..essential import book
#referecing for all requests in book
router = APIRouter(
    prefix = "/book",
)

get_db=database.get_db
#router for posting a newly created book
@router.post('/',status_code=201)
def create_book(request: schemas.Book,db:Session=Depends(get_db)):
   return book.create_book(request,db)
#router to get all available books
@router.get('/')
def get_all_books(db:Session=Depends(get_db)):
    return book.get_all_books(db)

#router to get a book by id
@router.get('/{id}',status_code=200)
def get_book(id,response:Response,db:Session=Depends(get_db)):
    return book.get_book(id,response,db)
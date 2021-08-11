from fastapi import FastAPI,Depends,status,Response,APIRouter
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..essential import user


router = APIRouter(prefix = "/user",)
get_db = database.get_db
#router to create a new user
@router.post('/')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
   
    return user.create_user(request,db)
#router to get a user by name
@router.get('/{name}',status_code=200)
def get_user(name,response:Response,db:Session=Depends(get_db)):
    return user.get_user(name,response,db)
#router to issue a book to a user.takes book id and name of the user as
#parameters
@router.put('/{name}/issue_book')
def issue_book(name,book_id:int,response:Response,db:Session=Depends(get_db),):
    return  user.issue_book(name,book_id,response,db)

#router tp return a book by a user.takes book id and name of the user as
#parameters
@router.put('/{name}/return_book')
def return_book(name,book_id:int,response:Response,db:Session=Depends(get_db),):
    return  user.return_book(name,book_id,response,db)

@router.get('/')
def get_all_users(db:Session=Depends(get_db)):
    return user.get_all_users(db)
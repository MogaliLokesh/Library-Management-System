from fastapi import FastAPI,Depends,status,Response,HTTPException
from .. import schemas,models
from sqlalchemy.orm import Session
from ..essential import book

get_book=book.get_book

def create_user(request:schemas.User,db:Session):
    new_user=models.User(name=request.name,mail=request.mail,books_in_hand=request.books_in_hand)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(name,response:Response,db:Session):
    user=db.query(models.User).filter(models.User.name==name).first()
    if not user:
        response.status_code=404

    return user

def issue_book(name:str,book_id:int,response:Response,db:Session):
    user=get_user(name,response,db)
    book=get_book(book_id,response,db)
    inventory = db.query(models.Inventory).filter(models.Inventory.id == book_id).first()
    
    if inventory.count==0:
         raise HTTPException(status_code=400,
                            detail=f'no copies of this book are currently available')
    if user.books_in_hand==3:
        raise HTTPException(status_code=404,
                            detail=f'user already posses maximum number of books')
   
    inventory.count=inventory.count-1
    user.books_in_hand=user.books_in_hand+1
    db.commit()
   
def return_book(name:str,book_id:int,response:Response,db:Session):
    user=get_user(name,response,db)
    book=get_book(book_id,response,db)
    inventory = db.query(models.Inventory).filter(models.Inventory.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404,
                            detail=f'please enter valid book id')
    inventory.count=inventory.count+1
    user.books_in_hand=user.books_in_hand-1
    db.commit()

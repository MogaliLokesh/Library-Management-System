from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database,models
from sqlalchemy.orm import Session


def create_book(request:schemas.Book,db:Session):
    new_book=models.Book(title=request.title)
    new_row=models.Inventory(count=request.number)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.add(new_row)
    db.commit()
    db.refresh(new_row)


    return new_book

def get_all_books(db:Session):
    books=db.query(models.Book).all()
    return books


def get_book(id,response:Response,db:Session):
    book=db.query(models.Book).filter(models.Book.id==id).first()
    if not book:
        response.status_code=400

    return book
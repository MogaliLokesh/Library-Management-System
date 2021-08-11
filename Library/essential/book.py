from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..import schemas,database,models
from sqlalchemy.orm import Session

#create a book, create corresponding column in inventoyry table and update
#database
def create_book(request:schemas.Book,db:Session):
    new_book = models.Book(title=request.title)
    new_inventory = models.Inventory(count=request.number)
    new_inventory.total_issues = 0
    db.add(new_book)
    db.add(new_inventory)
    db.commit()
    db.refresh(new_book)
    db.refresh(new_inventory)
    return new_book


#method to get all existing books
def get_all_books(db:Session):
    books = db.query(models.Book).all()
    return books


#get a centain book by id
def get_book(id,response:Response,db:Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=400,
                            detail=f'please enter a valid book')

    return book
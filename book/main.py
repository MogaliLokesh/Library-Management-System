from fastapi import FastAPI,Depends,status,Response
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/book',status_code=201)
def create_book(request: schemas.Book,db:Session=Depends(get_db)):
    new_book=models.Book(title=request.title)
    new_row=models.Inventory(count=request.number)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    db.add(new_row)
    db.commit()
    db.refresh(new_row)


    return new_book

@app.get('/book')
def get_all_books(db:Session=Depends(get_db)):
    books=db.query(models.Book).all()
    return books


@app.get('/book/{id}',status_code=200)
def get_book(id,response:Response,db:Session=Depends(get_db)):
    book=db.query(models.Book).filter(models.Book.id==id).first()
    if not book:
        response.status_code=400

    return book

@app.post('/user')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
    new_user=models.User(name=request.name,mail=request.mail,books_in_hand=request.books_in_hand)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user






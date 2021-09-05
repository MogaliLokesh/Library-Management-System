from fastapi import FastAPI,Depends,status,Response,HTTPException
from .. import schemas,models
from sqlalchemy.orm import Session
from ..essential import book
from sqlalchemy import and_
#importing get_book method
get_book = book.get_book


#method to create user and update in user table
def create_user(request:schemas.User,db:Session):
    new_user = models.User(name=request.name,mail=request.mail)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#get user based on the name of the user
def get_user(name,response:Response,db:Session):
    user = db.query(models.User).filter(models.User.name == name).first()
    if not user:
        raise HTTPException(status_code=404,
                            detail=f'please enter valid user name')

    return user


#issues book to an user.update user and inventory
def issue_book(name:str,book_id:int,response:Response,db:Session):
    user = get_user(name,response,db)
    book = get_book(book_id,response,db)
    inventory = db.query(models.Inventory).filter(models.Inventory.id == book_id).first()
  
    #raise an exception if the book has 0 copies currently in the inventor
    if inventory.count == 0:
         raise HTTPException(status_code=400,
                            detail=f'no copies of this book are currently available')
    #raise an exception if a user alredy posses 3 books and still make an isuue
    #request
    if user.books_in_hand == 3:
        raise HTTPException(status_code=404,
                            detail=f'user already posses maximum number of books')
    entry = db.query(models.AssociationUserBooks).filter(and_(models.AssociationUserBooks.book_id == book.id,models.AssociationUserBooks.user_name == user.name)).first()
    if not entry:
        new_entry = models.AssociationUserBooks(user_name=user.name,book_id=book.id)
        db.add(new_entry)
        
    else:
        entry.copies_in_hand = entry.copies_in_hand + 1
    
    inventory.count = inventory.count - 1
    
    inventory.total_issues = inventory.total_issues + 1
    user.books_in_hand = user.books_in_hand + 1
    db.commit()


#rerun book by a user.update user and inventory database
def return_book(name:str,book_id:int,response:Response,db:Session):
    user = get_user(name,response,db)
    book = get_book(book_id,response,db)
    inventory = db.query(models.Inventory).filter(models.Inventory.id == book_id).first()
    entry = db.query(models.AssociationUserBooks).filter(and_(models.AssociationUserBooks.book_id == book.id,models.AssociationUserBooks.user_name == user.name)).first()
    if not entry or entry.copies_in_hand == 0:
        raise HTTPException(status_code=404,
                            detail=f'user does not posses any copies of this book currently')
    entry.copies_in_hand = entry.copies_in_hand - 1
    inventory.count = inventory.count + 1
    user.books_in_hand = user.books_in_hand - 1
    db.commit()



#get all users in the Library database.
def get_all_users(db:Session):
    users = db.query(models.User).all()
    return users

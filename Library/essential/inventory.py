from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database,models
from sqlalchemy.orm import Session
from ..essential import book

##function that gives top 5 books in demand  in a separate table
def top_five_books_in_demand(response:Response,db:Session):
    book=db.query(models.Book)
    inventory = db.query(models.Inventory)
    #sorting inventory in descending order based on number of issues
    ans=inventory.order_by(models.Inventory.total_issues.desc()).limit(5).all()
    print(ans[0].id)
    #if entries already exits in top_five_books_in_demand table delete them all.
    popular_book=db.query(models.PopularBooks)
    if popular_book:
        popular_book.delete()
    #add each row of sorted inventory table into table with details such as book id, book name, total issues. 
    for an in ans:
        book=db.query(models.Book).filter(models.Book.id==an.id).first()
        new_row =models.PopularBooks(book_id=an.id,book_name=book.title,total_issues=an.total_issues)
        db.add(new_row)
        db.commit()
        db.refresh(new_row)
        

    

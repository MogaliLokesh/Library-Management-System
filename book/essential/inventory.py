from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database,models
from sqlalchemy.orm import Session
from ..essential import book


def top_five_books_in_demand(response:Response,db:Session):
    #return db.query(models.Book.title,models.Inventory.total_issues).filter(models.Inventory.id == models.Book.id).\
       #order_by(models.Inventory.total_issues.desc()).limit(5).all()
    book=db.query(models.Book)
    inventory = db.query(models.Inventory)
    ans=inventory.order_by(models.Inventory.total_issues.desc()).limit(5).all()
    print(ans[0].id)
    for an in ans:
        book=db.query(models.Book).filter(models.Book.id==an.id).first()
        new_row =models.PopularBooks(book_id=an.id,book_name=book.title,total_issues=an.total_issues)
        db.add(new_row)
        db.commit()
        db.refresh(new_row)

    

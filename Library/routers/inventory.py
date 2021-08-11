from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database
from sqlalchemy.orm import Session
from ..essential import inventory

router = APIRouter(prefix = "/inventory",tags=["Inventory"])


#import get_db from database
get_db = database.get_db


#route to get top 5 popular books
@router.get("/popular_books")
def top_five_books_in_demand(response:Response,db:Session(get_db)=Depends(get_db)):
    return inventory.top_five_books_in_demand(response,db)

#router to get entire inventory
@router.get('/')
def get_all_books(db:Session=Depends(get_db)):
    return inventory.get_inventory(db)
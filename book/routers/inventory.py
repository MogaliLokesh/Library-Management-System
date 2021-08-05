from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database
from sqlalchemy.orm import Session
from ..essential import inventory

router = APIRouter(
    prefix = "/inventory",
)

get_db=database.get_db

@router.get("/popular_books")
def top_five_books_in_demand(response:Response,db:Session(get_db)= Depends(get_db)):
    return inventory.top_five_books_in_demand(response,db)

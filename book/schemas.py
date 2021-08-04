 
from pydantic import BaseModel

class Book(BaseModel):
    title :str
    number:int


#class ShowBook(Book):
    #class Config():
        #orm_mode=True
class ShowBook(BaseModel):
    title:str

class User(BaseModel):
    name:str
    mail:str
    books_in_hand:int

class Inventory(BaseModel):
    count:int




 
from pydantic import BaseModel

class Book(BaseModel):
    title :str
    number:int
    
class User(BaseModel):
    name:str
    mail:str
    books_in_hand:int

class Inventory(BaseModel):
    count:int
    total_issues:int
   





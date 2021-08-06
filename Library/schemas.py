 
from pydantic import BaseModel
# defining pydantic schemas for book,user and inventory 
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
   




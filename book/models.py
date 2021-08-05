from .database import Base
from sqlalchemy import Column,Integer,String

class Book(Base):
    __tablename__='books'
    id= Column(Integer,primary_key=True,index=True)
    title= Column(String)

class User(Base):
    __tablename__='users'
    id= Column(Integer,primary_key=True,index=True)
    name= Column(String)
    mail=Column(String)
    books_in_hand=Column(Integer)

class Inventory(Base):
    __tablename__='inventory'
    id= Column(Integer,primary_key=True,index=True)
    count=Column(Integer)
    
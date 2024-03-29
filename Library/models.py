from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey

#sqlalchemy models for book,user,inventory and popular books tables.
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    mail = Column(String)
    books_in_hand = Column(Integer,default=0)

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer,primary_key=True,index=True)
    count = Column(Integer)
    total_issues = Column(Integer)
    

class  PopularBooks(Base):
    __tablename__ = 'top_five_books_in_demand'
    id = Column(Integer,primary_key=True,index=True)
    book_id = Column(String)
    book_name = Column(String)
    total_issues = Column(String)


class AssociationUserBooks(Base):
    __tablename__ = 'Association_User_Books'
    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String,ForeignKey("users.name"))
    book_id = Column(String,ForeignKey("books.id"))
    copies_in_hand = Column(Integer,default=1)
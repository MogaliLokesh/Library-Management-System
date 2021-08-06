from fastapi import FastAPI
from . import schemas,models
from .database import engine
from .routers import book,inventory,user
#get app intsanace of  fastapi 
app=FastAPI()
#create tables in the database
models.Base.metadata.create_all(engine)
#include routes of book,inventory,user in app
app.include_router(book.router)
app.include_router(inventory.router)
app.include_router(user.router)












from fastapi import FastAPI
from . import schemas,models
from .database import engine
from .routers import book,inventory,user

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(book.router)
app.include_router(inventory.router)
app.include_router(user.router)












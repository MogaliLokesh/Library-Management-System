from fastapi import APIRouter,Depends,status,Response
from ..import schemas,database
from sqlalchemy.orm import Session
from ..essential import inventory

router = APIRouter(
    prefix = "/inventory",
)
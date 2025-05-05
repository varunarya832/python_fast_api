from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter



router = APIRouter()

temp_arr = []

@router.get("/")
def read_root():
    return {"message": "Hello, World!"}

@router.post("/items/")
def create_item():
    global temp_arr
    temp_arr.append("New item")
    return {"message": "Item created", "items": temp_arr}
    
    
@router.get("/items/")
def read_items():
    return{"items":temp_arr}


class Item(BaseModel):
    item:str
    orders:int
    isplaced:bool= False

@router.post("/items2/")
def create_item2(cart : Item):
    global temp_arr
    temp_arr.append(cart)
    return {"message": "Item created", "items": temp_arr}

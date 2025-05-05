from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()



temp_arr: list[dict] = []



class Item(BaseModel):
    item: str
    orders: int
    isplaced: bool = False
    

@router.post("/create_item/")
def create_item(item: Item , status_code: int = 200):
    global temp_arr
    temp = item.dict()
    temp["id"] = len(temp_arr) + 1
    temp_arr.append(item.dict())
    return {"message": "Item created", "items": temp_arr}, status_code


@router.get("/get_items/")
def read_items():
    return {"items": temp_arr}


@router.delete("/get_item/{item_id}")
def delete_item(item_id: int):
    global temp_arr
    for i in temp_arr:
        if i["id"] == item_id:
            temp_arr.remove(i)
            return {"message": "Item deleted", "items": temp_arr}


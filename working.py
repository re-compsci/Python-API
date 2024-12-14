from fastapi import FastAPI, Path, Query, HTTPException,status  
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] =  None

    
class UpdateItem(BaseModel):
    name: Optional[str] =  None
    price: Optional[float] =  None 
    brand: Optional[str] =  None


inventorty = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description= "The ID of the item you'd like to view")):
    for item_id in inventorty:
        if item_id in inventorty[item_id]:
            return inventorty[item_id]
    raise HTTPException(404,"Item ID not found.")      


@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int ,name: Optional[str] = None , test: int):
    for item_id in inventorty:
        if inventorty[item_id].name == name :
            return inventorty[item_id]
    raise HTTPException(404,"Item name not found.")      
    #return {"Data":"Not Found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int,item: Item):
    if item_id in inventorty:
          raise HTTPException(302,"Item ID already exists.") 
       #return{"Error":"Item ID already exists."} 

    inventorty[item_id] = item 
    #{"name": item.name, "price": item.price, "brand": item.brand}
    return inventorty[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventorty:
          raise HTTPException(404,"Item ID doesn't exists.")  

    if item.name != None:
        inventorty[item_id].name = item.name
    if item.price != None:
        inventorty[item_id].price = item.price
    if item.brand != None:
        inventorty[item_id].brand = item.brand

   #inventorty[item_id]=item
    return inventorty[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(...,description="The ID of the item to delete.")):
    if item_id not in inventorty:
        raise HTTPException(404,"Item ID doesn't exists.") 
        #return{"Error":"Item ID doesn't exists."} 
    del inventorty[item_id]
    raise HTTPException(200,"Item deleted!") 
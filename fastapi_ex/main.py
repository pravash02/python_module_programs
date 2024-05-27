"""
pravashpanigrahi@Pravashs-MacBook-Air fastapi_ex % uvicorn main:app --reload
curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
curl -X GET http:/ /127.0.0.1:8000/items/0
curl -X GET http:/ /127.0.0.1:8000/items/indian
"""

from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class AvailableItems(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

items = []

food_items = {
    'indian': ['food_ind1', 'food_ind2'],
    'american': ['food_am1', 'food_am2']
}

@app.get("/")
def root():
    return {'payload': 'Hello API'}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

# @app.get("/items/{item_id}")
# def get_item(item_id: int) -> str:
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise Exception(f"{item_id} not found")

@app.get("/items/{item_name}")
async def get_items(item_name: AvailableItems):
    return food_items.get(item_name)

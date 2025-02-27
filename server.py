from fastapi import FastAPI

app = FastAPI()

# Sample data array
data = [
    {"id": 1, "name": "Item 1", "description": "Description 1"},
    {"id": 2, "name": "Item 2", "description": "Description 2"},
    {"id": 3, "name": "Item 3", "description": "Description 3"},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    for i in data:
        if i["id"] == item_id:
            result = i
            break
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    if q:
        filtered_data = []
        for i in data:
            if q.lower() in i["name"].lower() or q.lower() in i["description"].lower():
                filtered_data.append(item)
        result["filtered_data"] = filtered_data
    return result


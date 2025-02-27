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
    # Inefficiently search for the item in the array
    for item in data:
        if item["id"] == item_id:
            result = item
            break
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    # Inefficiently filter the data based on the query parameter
    if q:
        filtered_data = []
        for item in data:
            if q.lower() in item["name"].lower() or q.lower() in item["description"].lower():
                filtered_data.append(item)
        result["filtered_data"] = filtered_data
    return result


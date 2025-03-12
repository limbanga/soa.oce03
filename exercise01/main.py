from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import HTTPException

app = FastAPI()

class Item(BaseModel):
    price: float = Field(..., gt=0)

@app.post("/items/{item_id}")
async def get_item(
    item_id: int = Path(..., gt=0),
    category: Optional[str] = Query(None),
    item: Item = None
):
    if item is None:
        raise HTTPException(status_code=400, detail="Price is required in the request body.")
    
    return {
        "item_id": item_id,
        "category": category,
        "price": item.price
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

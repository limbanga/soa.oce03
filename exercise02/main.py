from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Cart(BaseModel):
    user_id: int = Field(..., gt=0)
    items: List[str] = Field(..., min_items=1)

@app.post("/cart/")
async def create_cart(cart: Cart):
    return cart

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., ge=1)
    price: float = Field(..., gt=0)

class Order(BaseModel):
    customer_id: int = Field(..., gt=0)
    order_items: List[OrderItem] = Field(..., min_items=1)

@app.post("/order/")
async def create_order(order: Order):
    return order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
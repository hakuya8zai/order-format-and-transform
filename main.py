from fastapi import FastAPI
from asiaYo.app.api.order import router as order_router

app = FastAPI()

app.include_router(order_router, prefix="/api/orders", tags=["orders"])


@app.get("/")
def read_root():
    return {
        "documentation": "Visit /docs for the interactive API documentation and testing interface.",
        "try_api": "Try posting to /api/orders to create a new order.",
    }

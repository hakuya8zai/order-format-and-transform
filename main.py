from fastapi import FastAPI
from asiaYo.app.api.order import router as order_router

app = FastAPI()

app.include_router(order_router, prefix="/api/orders", tags=["orders"])

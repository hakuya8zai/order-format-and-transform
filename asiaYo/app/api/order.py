from fastapi import APIRouter, HTTPException
from asiaYo.order.schemas.order_schemas import OrderSchema
from asiaYo.order.models.order_models import Order
from asiaYo.order.order_services import OrderService

router = APIRouter()

@router.post("/", response_model=Order)
def create_order(order: OrderSchema):
    try:
        order_service = OrderService()
        return order_service.process_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

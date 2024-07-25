from fastapi import APIRouter, HTTPException, Depends
from asiaYo.order.models.order_models import Order
from asiaYo.order.schemas.order_schemas import OrderSchema
from asiaYo.order.order_services import OrderService
from asiaYo.order.order_dependencies import get_order_service

router = APIRouter()


@router.post("/", response_model=Order)
def create_order(
    order: OrderSchema, order_service: OrderService = Depends(get_order_service)
):
    try:
        processed_order = order_service.process_order(order)
        return processed_order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

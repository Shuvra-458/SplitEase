from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.settlement import SettlementCreate
from app.services.settlement_service import settle_balance

router = APIRouter(
    prefix="/settlements",
    tags=["settlements"]
)

@router.post("")
def create_settlement(payload: SettlementCreate, db: Session = Depends(get_db)):
    try:
        settle_balance(
            db,
            payload.from_user,
            payload.to_user,
            payload.amount
        )
        return {"status": "settled"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
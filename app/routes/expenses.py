from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.expense import ExpenseCreate
from app.services.expense_service import add_expense

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post("", status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    try:
        expense_id = add_expense(db, expense)
        return {"expense_id": expense_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


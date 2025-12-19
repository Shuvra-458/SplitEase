from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.balance import Balance

router = APIRouter(
    prefix="/balances",
    tags=["Balances"]
)

@router.get("/users/{user_id}")
def get_user_balance(user_id: int, db: Session = Depends(get_db)):
    owes = db.query(Balance).filter(Balance.from_user == user_id).all()
    gets = db.query(Balance).filter(Balance.to_user == user_id).all()

    return {
        "user_id": user_id,
        "owes": [
            {"to": b.to_user, "amount": float(b.amount)}
            for b in owes
        ],
        "gets_back": [
            {"from": b.from_user, "amount": float(b.amount)}
            for b in gets
        ]
    }

@router.get("/groups/{group_id}")
def get_group_balances(group_id: int, db: Session = Depends(get_db)):
    balances = db.query(Balance).filter(Balance.group_id == group_id).all()

    return [
        {
            "from": b.from_user,
            "to": b.to_user,
            "amount": float(b.amount)
        }
        for b in balances
    ]

from sqlalchemy.orm import Session
from app.models.balance import Balance
from app.models.settlement import Settlement
from decimal import Decimal

def settle_balance(db: Session, from_user: int, to_user: int, amount: float):
    
    balance = db.query(Balance).filter_by(
        from_user=from_user,
        to_user=to_user
    ).first()

    if not balance:
        raise ValueError("No balance exists to settle")
    if amount > float(balance.amount):
        raise ValueError("Settlement amount exceeds outstanding balance")
    
    settlement_amount = Decimal(str(amount))
    balance.amount -= settlement_amount

    if balance.amount == 0:
        db.delete(balance)
    
    settlement = Settlement(
        from_user=from_user,
        to_user=to_user,
        amount=amount
    )

    db.add(settlement)
    db.commit()


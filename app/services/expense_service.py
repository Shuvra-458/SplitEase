from sqlalchemy.orm import Session

from app.models.expense import Expense, SplitType
from app.models.expense_split import ExpenseSplit
from app.models.balance import Balance
from app.models.group_member import GroupMember

from app.services.split_strategies.equal import EqualSplitStrategy
from app.services.split_strategies.exact import ExactSplitStrategy
from app.services.split_strategies.percent import PercentSplitStrategy

STRATEGY_MAP = {
    "EQUAL": EqualSplitStrategy(),
    "EXACT": ExactSplitStrategy(),
    "PERCENT": PercentSplitStrategy(),
}

def add_expense(db: Session, payload):
    #validation of users belonging to a group
    member_ids = {
        m.user_id
        for m in db.query(GroupMember)
        .filter(GroupMember.group_id == payload.group_id)
        .all()
    }

    split_user_ids = {s.user_id for s in payload.splits}

    if not split_user_ids.issubset(member_ids):
        raise ValueError("All split users must belong to the group")
    
    #Creating Expense
    expense = Expense(
        description=payload.description,
        amount=payload.amount,
        paid_by=payload.paid_by,
        group_id=payload.group_id,
        split_type=payload.split_type
    )

    db.add(expense)
    db.flush()

    #Calculating Splits
    strategy = STRATEGY_MAP[payload.split_type.value]

    split_data = [
        s.dict(exclude_unset=True)
        for s in payload.splits
    ]
    split_result = strategy.calculate(payload.amount, split_data)

    #Storing Expense Splits
    for user_id, amount in split_result.items():
        db.add(
            ExpenseSplit(
                expense_id=expense.id,
                user_id=user_id,
                amount=amount
            )
        )

        #Updating the Balances
        if user_id == payload.paid_by:
            continue
        balance = db.query(Balance).filter_by(
            from_user=user_id,
            to_user=payload.paid_by,
            group_id=payload.group_id
        ).first()

        if balance:
            balance.amount += amount
        else:
            db.add(
                Balance(
                    from_user=user_id,
                    to_user=payload.paid_by,
                    group_id=payload.group_id,
                    amount=amount
                )
            )
    db.commit()
    return expense.id

from sqlalchemy import Column, Integer, ForeignKey, Numeric, UniqueConstraint
from app.database import Base

class Balance(Base):
    __tablename__ = "balances"

    id = Column(Integer, primary_key=True)
    from_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    to_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("expense_groups.id"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)

    __table_args__ = (
        UniqueConstraint("from_user", "to_user", "group_id", name="unique_balance"),
    )
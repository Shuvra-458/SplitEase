from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime, Numeric
from sqlalchemy.sql import func
from app.database import Base
import enum

class SplitType(enum.Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    paid_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    group_id = Column(Integer, ForeignKey("expense_groups.id"), nullable=False)
    split_type = Column(Enum(SplitType), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
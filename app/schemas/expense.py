from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class SplitType(str, Enum):
    EQUAL = "EQUAL"
    EXACT = "EXACT"
    PERCENT = "PERCENT"

class ExpenseSplitInput(BaseModel):
    user_id: int
    amount: Optional[float] = None
    percent: Optional[float] = None

class ExpenseCreate(BaseModel):
    description: str
    amount: float
    paid_by: int
    group_id: int
    split_type: SplitType
    splits: List[ExpenseSplitInput]
from pydantic import BaseModel
from typing import List

class BalanceItem(BaseModel):
    user_id: int
    amount: float

class UserBalanceResponse(BaseModel):
    user_id: int
    owes: List[BalanceItem]
    gets_back: List[BalanceItem]
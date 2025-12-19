from pydantic import BaseModel

class SettlementCreate(BaseModel):
    from_user: int
    to_user: int
    amount: float
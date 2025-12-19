from pydantic import BaseModel
from typing import List

class GroupCreate(BaseModel):
    name: str
    created_by: int
    member_ids: List[int]

class GroupResponse(BaseModel):
    id: int
    name: str
    members: List[int]
    
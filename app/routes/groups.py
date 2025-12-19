from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.group import Group
from app.models.group_member import GroupMember
from app.models.user import User
from app.schemas.group import GroupCreate, GroupResponse

router = APIRouter(
    prefix="/groups",
    tags = ["Groups"]
)

@router.post("", response_model=GroupResponse, status_code=status.HTTP_201_CREATED)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    creator = db.query(User).filter(User.id == group.created_by).first()
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    
    if group.created_by not in group.member_ids:
        raise HTTPException(status_code=400, detail="Creator must be in group")
    
    new_group = Group(
        name=group.name,
        created_by=group.created_by
    )

    db.add(new_group)
    db.commit()
    db.refresh(new_group)

    for uid in set(group.member_ids):
        db.add(GroupMember(group_id=new_group.id, user_id=uid))
    
    db.commit()

    return GroupResponse(
        id = new_group.id,
        name = new_group.name,
        members = group.member_ids
    )

@router.get("/{group_id}", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Group Not Found")
    
    members = (
        db.query(GroupMember.user_id)
        .filter(GroupMember.group_id == group_id)
        .all()
    )
    member_ids = [m.user_id for m in members]

    return GroupResponse(
        id=group_id,
        name=group.name,
        members=member_ids
    )
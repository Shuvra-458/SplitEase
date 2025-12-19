from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Settlement(Base):
    __tablename__ = "settlements"

    id = Column(Integer, primary_key=True)
    from_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    to_user = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
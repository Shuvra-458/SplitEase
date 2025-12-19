from app.database import engine
from app.models.user import User
from app.models.group import Group
from app.models.group_member import GroupMember
from app.models.expense import Expense
from app.models.expense_split import ExpenseSplit
from app.models.balance import Balance
from app.models.settlement import Settlement

from app.database import Base

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")

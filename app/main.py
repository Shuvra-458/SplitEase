from fastapi import FastAPI
from app.routes import groups, users, expenses, balances, settlements

app = FastAPI(title="CredResolve API")

app.include_router(users.router)
app.include_router(groups.router)
app.include_router(expenses.router)
app.include_router(balances.router)
app.include_router(settlements.router)


# SplitEase 🧾💸

SplitEase is a Splitwise-like expense sharing application built using **FastAPI** and **PostgreSQL**.
Try the backend at:
https://splitease-vaun.onrender.com/docs
---

## 🚀 Features

- User and group management
- Expense creation with multiple split strategies:
  - Equal
  - Exact
  - Percent
- Incremental balance calculation (no recomputation)
- Partial and full settlements
- Audit trail for settlements
- Clean, modular, service-based architecture

---

## 🧠 Architecture Overview

- **FastAPI** – API layer
- **SQLAlchemy (sync)** – ORM
- **PostgreSQL** – Relational database
- **Pydantic** – Request/response validation
- **Strategy Pattern** – Expense split logic
- **Service Layer** – Business logic isolation

---

## 📁 Project Structure

```
app/
├── main.py
├── database.py
├── models/
├── schemas/
├── routes/
├── services/
│   └── split_strategies/
└── utils/
```

---

## 🛠️ Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/Shuvra-458/SplitEase.git
cd SplitEase
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup environment variables
Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/splitease
```

### 5. Create database tables
```bash
python -m app.create_tables
```

### 6. Run the server
```bash
uvicorn app.main:app --reload
```

---

## 🔗 API Documentation

Once the server is running, access Swagger UI at:

```
http://127.0.0.1:8000/docs
```

---

## ⚖️ Design Decisions

- Balances are updated at write time for **O(1)** reads
- Monetary values are handled using **Decimal** to avoid precision issues
- Strategy pattern allows easy extension of split logic
- Transactions ensure consistency and data integrity

---

## 🔮 Future Improvements

- Authentication & authorization
- Expense editing and deletion
- Multi-currency support
- Async database support
- Background reconciliation jobs

---


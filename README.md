 FastAPI User Management API

A simple FastAPI project with PostgreSQL and Alembic for migrations.

---

## Quick Start

### 1️⃣ Install Dependencies
```bash
pip install fastapi
pip install uvicorn[standard]
pip install sqlalchemy
pip install psycopg2-binary
pip install pydantic
pip install alembic
2️⃣ Run the App
bash
Copy code
uvicorn app.main:app --reload
3️⃣ Apply Database Migrations
bash
Copy code
alembic upgrade head
4️⃣ Test Endpoints
Open in browser:

arduino
Copy code
http://127.0.0.1:8000/docs
Use Swagger UI to interact with all endpoints

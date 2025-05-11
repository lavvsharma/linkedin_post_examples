from fastapi import FastAPI, Depends
from sqlalchemy import text
from .database import get_db

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI app with PostgreSQL is running!"}

@app.get("/ping-db")
def ping_db(db=Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar()
        return {"status": "Database connected!"} if result == 1 else {"status": "DB not OK"}
    except Exception as e:
        return {"status": "DB connection failed", "error": str(e)}

from fastapi import FastAPI
from src.db.database import db_connection


app = FastAPI()
db_connection()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)


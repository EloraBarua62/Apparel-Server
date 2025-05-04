from fastapi import FastAPI
from src.db.database import init_db
from src.controllers.user_controller import router as user_router


app = FastAPI()
app.include_router(user_router, prefix="/api/v1/user", tags=["Users"])

# Initialize DB once at startup
@app.on_event("startup")
def startup_event():
    init_db()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=5000)


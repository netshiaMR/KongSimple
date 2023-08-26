from fastapi import FastAPI
from app.database import metadata, engine, DATABASE_URL
from app.routers import customer
from app.logging_config import setup_logging
import uvicorn

metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.router, prefix="/customers", tags=["customers"])

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    setup_logging()
    logging.info("Starting the application...")
    run()

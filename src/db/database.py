import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine.url import URL
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Validate required environment variables
required_vars = ["DB_USER", "DB_PASSWORD", "DB_HOST", "DB_NAME"]
for var in required_vars:
    if not os.getenv(var):
        raise ValueError(f"Environment variable {var} is not set or empty")

# Prepare database connection details
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# Use URL.create for reliable formatting
# DATABASE_URL_WITHOUT_DB = str(URL.create(
#     drivername="mysql+pymysql",
#     username=DB_USER,
#     password=DB_PASSWORD,
#     host=DB_HOST
# ))

DATABASE_URL_WITHOUT_DB = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}"
)

# Set up SQLAlchemy Base
Base = declarative_base()

# Function to ensure database exists
def create_database_if_not_exists():
    engine_temp = create_engine(DATABASE_URL_WITHOUT_DB)
    with engine_temp.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))
    engine_temp.dispose()

# # Create DB if missing
# create_database_if_not_exists()



# Set up SQLAlchemy engine
_engine = None

def get_engine():
    global _engine

    # Complete database URL with DB name
    DATABASE_URL = f"{DATABASE_URL_WITHOUT_DB}/{DB_NAME}"
    if _engine is None:
        _engine = create_engine(DATABASE_URL)
    return _engine


# Set up session
SessionLocal = sessionmaker(bind=get_engine(), autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize database (create DB and tables)
def init_db():
    from src.models.user_model import Base  # Ensure all models are imported before creating tables
    create_database_if_not_exists()
    engine = get_engine()
    Base.metadata.create_all(bind=engine)


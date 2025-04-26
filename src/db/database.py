# MySQL driver “MySQL Connector” to access the MySQL database
import mysql.connector
from mysql.connector import Error
import os
from src.utils.response import api_response
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# 

# Create a connection to MySQL database
def db_connection():
    "Create a connection to MySQL database"
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'))
        api_response(200, "Database connection successful")
        return connection
    except Error as e:
        api_response(500, "Database connection error", str(e))
        







                                             

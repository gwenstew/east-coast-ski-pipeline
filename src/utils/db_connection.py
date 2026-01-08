import psycopg2
from src.utils.config import DB_CONFIG


def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def connect_to_db():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        print("Connection to postgres DB successful")
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return

def get_cursor():
    connection = get_connection()
    return connection.cursor()

import psycopg
from config import Config

# seconds to wait for the database before giving up 
DB_CONNECT_TIMEOUT = 30

def get_db_connection():
    conn = psycopg.connect(
        Config.DATABASE_URL.replace("+psycopg", "", 1),
        connect_timeout=DB_CONNECT_TIMEOUT
    )
    return conn
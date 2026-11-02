import psycopg
from config import Config

def get_db_connection():
    conn = psycopg.connect(Config.DATABASE_URL.replace("+psycopg", "", 1))
    return conn
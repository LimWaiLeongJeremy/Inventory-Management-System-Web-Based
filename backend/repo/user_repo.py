from database.db import get_db_connection
from .query.user_qry import IST_USR_QRY
from datetime import datetime
# from models.user_model import User

def ist_usr_repo(
    username, 
    fullname,
    hashed_password,
    role
    ):

    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        try:
            cursor.execute(IST_USR_QRY, (
                username,
                fullname,
                hashed_password,
                True,
                datetime.now(),
                role
            ))
            new_id = cursor.fetchone()[0]
            conn.commit()
            return True, new_id
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        raise
    finally:    
        conn.close()

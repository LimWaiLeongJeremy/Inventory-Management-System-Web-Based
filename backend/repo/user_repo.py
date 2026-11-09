import traceback

from database.db import get_db_connection
from .query.user_qry import IST_USR_QRY, SEL_USR_BY_NAME
from datetime import datetime
from models.user_model import User

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
        traceback.print_exc()
        raise
    finally:    
        conn.close()


def get_user_by_username(
    username
    ):
    
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        try:
            cursor.execute(SEL_USR_BY_NAME, (
                username,
            ))
            row = cursor.fetchone()
            if row is None:
                return False, None

            # Setting User model
            columns = [desc[0] for desc in cursor.description]
            user = User.from_row(columns, row)

            conn.commit()
            return True, user
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:    
        conn.close()

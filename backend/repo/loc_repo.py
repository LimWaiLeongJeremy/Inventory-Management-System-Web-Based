import traceback

from database.db import get_db_connection
from .query.loc_qry import GET_LOCATIONS
from models.loc_model import Location

def get_locations_repo():
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_LOCATIONS).fetchall()

            # Setting model
            columns = [desc[0] for desc in cursor.description]
            locations = [Location.from_row(columns, row) for row in rows]

            conn.commit()
            return True, locations
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close()
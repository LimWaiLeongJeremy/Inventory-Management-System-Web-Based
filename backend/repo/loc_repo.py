from database.db import get_db_connection
from .query.loc_qry import GET_LOCATIONS
from models.loc_model import Location

def get_locations_repo():
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_LOCATIONS)

            locations = [
                Location(
                    id = row[0], 
                    code = row[1], 
                    name = row[2], 
                    is_active = row[3]
                )
                for row in rows
            ]

            conn.commit()
            return locations
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close()
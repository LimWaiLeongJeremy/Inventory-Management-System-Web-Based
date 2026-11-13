import traceback

from database.db import get_db_connection
from .query.loc_qry import GET_ALL_LOCATIONS, GET_ZONE_BY_LOC, GET_LOC_EXIST
from models.loc_model import Location, Zone

def get_all_locations_repo():
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_ALL_LOCATIONS).fetchall()

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

def get_loc_exist_repo(location_code):
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        try:
            exists = cursor.execute(GET_LOC_EXIST, (location_code,)).fetchone()[0]

            conn.commit()
            return exists
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close()
    

def get_zone_by_loc_repo(location_code):
    conn = get_db_connection()
    
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_ZONE_BY_LOC, (location_code,)).fetchall()

            # Setting model
            columns = [desc[0] for desc in cursor.description]
            locations = [Zone.from_row(columns, row) for row in rows]

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
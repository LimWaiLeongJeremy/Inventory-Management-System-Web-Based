import traceback

from database.db import get_db_connection
from repo.loc_repo import get_all_locations_repo, get_zone_by_loc_repo, get_loc_exist_repo, get_bin_by_zone_repo

def get_locations_svc():
    conn = get_db_connection()
    try:
        status, result = get_all_locations_repo(conn)
        # Check if data exists
        print("loc")
        if not result:
            return False, "could not find location"
        return status, result
    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise     
    finally:
        conn.close()


def get_zone_by_loc_svc(location_code):
    conn = get_db_connection()
    try:
        # Check if location exists
        exists = get_loc_exist_repo(conn, location_code)
        if not exists:
            return exists, "Location cannot be found" 

        status, result = get_zone_by_loc_repo(conn, location_code)
        # Check if data exists
        if not result:
            return False, "Zone cannot be found"
        return status, result

    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise     
    finally:
        conn.close()  


def get_bin_by_zone_svc(location_code, zone_id):
    conn = get_db_connection()
    try:
        status, result = get_bin_by_zone_repo(
            conn,
            location_code, 
            zone_id
        )
        # Check if data exists
        if not result:
            return False, "could not find bins"
        return status, result

    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise     
    finally:
        conn.close()  
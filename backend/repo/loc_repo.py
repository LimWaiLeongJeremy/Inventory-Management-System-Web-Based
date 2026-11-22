import traceback

from database.db import get_db_connection
from .query.loc_qry import GET_ALL_LOCATIONS, GET_ZONE_BY_LOC, GET_LOC_EXIST, GET_BIN_BY_ZONE
from models.loc_model import Location, Zone, Bin

def get_all_locations_repo(conn):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(GET_ALL_LOCATIONS).fetchall()

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        locations = [Location.from_row(columns, row) for row in rows]

        return True, locations
    finally:
        cursor.close()

def get_loc_exist_repo(conn, location_code):
    cursor = conn.cursor()
    try:
        # Execute query
        exists = cursor.execute(GET_LOC_EXIST, (location_code,)).fetchone()[0]
        return exists
    finally:
        cursor.close()
    

def get_zone_by_loc_repo(conn, location_code):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(GET_ZONE_BY_LOC, (location_code,)).fetchall()

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        locations = [Zone.from_row(columns, row) for row in rows]

        return True, locations
    finally:
        cursor.close()

def get_bin_by_zone_repo(conn, location_code, zone_id):
    cursor = conn.cursor()
    try:
        rows = cursor.execute(GET_BIN_BY_ZONE, (location_code, zone_id,)).fetchall()

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        bins = [Bin.from_row(columns, row) for row in rows]

        return True, bins
    finally:
        cursor.close()

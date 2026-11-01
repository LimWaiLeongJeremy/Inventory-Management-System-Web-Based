from database.db import get_db_connection
from .query.loc_qry import GET_LOCATIONS
from models.loc_model import Location

def get_locations():
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute(GET_LOCATIONS)

    locations = [
        Location(row[0], row[1], row[2], row[3])
        for row in rows
    ]
    
    cursor.close()
    conn.close()

    return locations
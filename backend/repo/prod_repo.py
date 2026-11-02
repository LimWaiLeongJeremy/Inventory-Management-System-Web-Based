from database.db import get_db_connection
from .query.prod_qry import GET_PRODUCT_BY_LOCATION
from models.prod_model import Product

def get_product_by_location(location):
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute(GET_PRODUCT_BY_LOCATION, (location,))

    products = [
        Product(
            location = row[0], 
            barcode = row[1],
            name = row[2],
            category = row[3],
            unit = row[4],
            reorder_level = row[5],
            quantity = row[6]
        )
        for row in rows
    ]

    cursor.close()
    conn.close()

    return products
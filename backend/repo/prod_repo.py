import traceback

from .query.prod_qry import (
    GET_PRODUCT_BY_LOCATION_ZONE_BIN, 
    GET_LOCATION_BY_PRODUCT
)
from models.prod_model import Product

def get_product_by_location_zone_bin_repo(
    conn, 
    location_code, 
    zone_id, 
    bin_id
):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            GET_PRODUCT_BY_LOCATION_ZONE_BIN, 
            (location_code, zone_id, bin_id,)).fetchall()

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        products = [Product.from_row(columns, row) for row in rows]

        return True, products
    finally:
        cursor.close()


def get_location_by_product_repo(conn, product_name):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            GET_LOCATION_BY_PRODUCT, 
            (product_name,))

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        products = [Product.from_row(columns, row) for row in rows]

        return True, products
    finally:
        cursor.close()

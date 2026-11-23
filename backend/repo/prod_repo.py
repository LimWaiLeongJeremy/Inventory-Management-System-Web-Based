import traceback

from .query.prod_qry import (
    GET_PRODUCT_BY_LOCATION_ZONE_BIN, 
    GET_LOCATION_BY_PRODUCT,
    GET_ALL_PRODUCTS
)
from models.prod_model import Product, All_Product

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




def get_all_products(db):
    cursor = db.cursor()

    try:
        cursor.execute(GET_ALL_PRODUCTS)

        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        products = [
            All_Product.from_row(columns, row)
            for row in rows
        ]
        return products
    finally:
        cursor.close()

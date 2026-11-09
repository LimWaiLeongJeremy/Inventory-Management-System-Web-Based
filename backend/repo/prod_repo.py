import traceback

from database.db import get_db_connection
from .query.prod_qry import GET_PRODUCT_BY_LOCATION, GET_LOCATION_BY_PRODUCT
from models.prod_model import Product

def get_product_by_location_repo(location):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_PRODUCT_BY_LOCATION, (location,)).fetchall()

            # Setting model
            columns = [desc[0] for desc in cursor.description]
            products = [Product.from_row(columns, row) for row in rows]

            conn.commit()
            return True, products
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close()

def get_location_by_product_repo(product_name):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        try:
            rows = cursor.execute(GET_LOCATION_BY_PRODUCT, (product_name,))

            # Setting model
            columns = [desc[0] for desc in cursor.description]
            products = [Product.from_row(columns, row) for row in rows]

            conn.commit()
            return True, products
        finally:
            cursor.close()
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close()
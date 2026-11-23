import traceback

from database.db import get_db_connection
from repo.prod_repo import (
    get_product_by_location_zone_bin_repo, 
    get_location_by_product_repo,
    get_all_products
)

def get_product_by_location_zone_bin_svc(
    location_code, 
    zone_id, 
    bin_id
):
    conn = get_db_connection()
    try:
        status, result = get_product_by_location_zone_bin_repo(
            conn, location_code, zone_id, bin_id)
        # Check if data exists
        if not result:
            return False, "Invalid location"
        
        return status, result
    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close() 
    

def get_location_by_product_svc(product_name):
    conn = get_db_connection()
    try:
        status, result = get_location_by_product_repo(
            conn, product_name)
        # Check if data exists
        if not result:
            return False, "Invalid product"
        
        return status, result
    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close() 



def get_all_products_svc():
    conn = get_db_connection()

    try:
        products = get_all_products(conn)

        # Check if products exist
        if not products:
            return False, "No products found"

        return True, products

    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise

    finally:
        conn.close()
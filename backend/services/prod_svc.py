import traceback

from database.db import get_db_connection
from repo.prod_repo import (
    get_product_by_location_zone_bin_repo, 
    get_location_by_product_repo,
    get_current_stock_by_id_repo,
    ist_outbound_repo
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
    

# Stock transfer
def stock_transfer_svc(location_id, product_barcode, quantity):
    conn = get_db_connection()
    try:
        # Get and lock product 
        status, pre_trns_result = get_current_stock_by_id_repo(
            conn, location_id, product_barcode)
        # Check if data exists
        if not status:
            return status, "Invalid product"

        # insert outbound record
        ist_out_success = ist_outbound_repo(
            conn, quantity, product_barcode, location_id)
        if not ist_out_success:
            return ist_out_success, "Insert outbound record failed"
        
        # For testing
        status, post_trns_result = get_current_stock_by_id_repo(
            conn, location_id, product_barcode)

        # TODO
        # Change to commit
        conn.rollback()
        return status, post_trns_result
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


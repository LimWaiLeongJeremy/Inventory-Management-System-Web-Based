import traceback

from database.db import get_db_connection
from repo.prod_repo import (
    get_product_by_location_zone_bin_repo, 
    get_location_by_product_repo,
    get_current_stock_by_id_repo,
    ist_outbound_repo,
    ist_inbound_repo
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
def stock_transfer_svc(from_location_id, to_location_id, product_barcode, quantity, bin_id):
    conn = get_db_connection()
    try:
        # Get and lock product 
        status, pre_trns_result = get_current_stock_by_id_repo(
            conn, from_location_id, product_barcode)
        # Check if data exists
        if not status:
            return status, "Invalid product"

        # insert outbound record
        ist_out_success = ist_outbound_repo(
            conn, quantity, product_barcode, from_location_id)
        if not ist_out_success:
            conn.rollback()
            return ist_out_success, "Insert outbound record failed"
        status, source_result = get_current_stock_by_id_repo(
            conn, from_location_id, product_barcode)

        # TODO 
        # get first inbound bin for all location
        # insert inbound record
        ist_in_success = ist_inbound_repo(
            conn, quantity, product_barcode, to_location_id, bin_id)
        if not ist_in_success:
            conn.rollback()
            return dest_success, "Insert inbound record failed"

        # For testing
        status, post_trns_result = get_current_stock_by_id_repo(
            conn, to_location_id, product_barcode)

        result = {
            "source": [stk.to_dict() for stk in source_result],
            "destination": [stk.to_dict() for stk in dest_result],
        }
        # TODO
        # Change to commit
        conn.rollback()
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


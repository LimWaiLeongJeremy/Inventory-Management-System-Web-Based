import traceback

from database.db import get_db_connection
from repo.prod_repo import (
    get_product_by_location_zone_bin_repo, 
    # get_location_by_product_repo,
    get_all_products,
    get_current_stock_by_id_repo,
    ist_outbound_repo,
    ist_inbound_repo,
    ist_txn_logs_repo,
    get_product_transfer_eligibility_repo
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
def stock_transfer_svc(
        from_location_id, 
        to_location_id, 
        product_barcode, 
        quantity, 
        bin_id,
        reference,
        note,
        user_id
    ):
    conn = get_db_connection()
    try:
        # Get and lock product 
        source_exists, pre_trns_result = get_current_stock_by_id_repo(
            conn, from_location_id, product_barcode)
        # Check if data exists
        if not source_exists:
            return source_exists, "Invalid product"
        
            # Check for transfer eligibility
        eligible = get_product_transfer_eligibility_repo(
            conn,
            quantity,
            from_location_id,
            product_barcode
        )
        if not eligible:
            return False, (
                f"Not enough stock for product ID:{product_barcode} "
                f"at location ID:{from_location_id}"
            )

        # insert outbound record
        ist_out_success = ist_outbound_repo(
            conn, quantity, product_barcode, from_location_id)
        if not ist_out_success:
            conn.rollback()
            return ist_out_success, "Insert outbound record failed"
        source_updated, source_result = get_current_stock_by_id_repo(
            conn, from_location_id, product_barcode)

        # TODO 
        # get first inbound bin for all location
        # insert inbound record
        ist_in_success = ist_inbound_repo(
            conn, quantity, product_barcode, to_location_id, bin_id)
        if not ist_in_success:
            conn.rollback()
            return ist_in_success, "Insert inbound record failed"

        ist_txn_logs_success = ist_txn_logs_repo(
            conn,
            "TRANSFER",
            product_barcode,
            from_location_id,
            to_location_id,
            quantity,
            reference,
            note,
            user_id
        )
        if not ist_txn_logs_success:
            conn.rollback()
            return False, "Insert transaction log failed"

        dest_updated, dest_result = get_current_stock_by_id_repo(
            conn, to_location_id, product_barcode)

        result = {
            "source": [stk.to_dict() for stk in source_result],
            "destination": [stk.to_dict() for stk in dest_result],
            "logs": ist_txn_logs_success
        }
        # TODO
        # Change to commit
        conn.rollback()
        return True, result
    # Raise exception if failed
    except Exception:
        conn.rollback()
        traceback.print_exc()
        raise
    finally:
        conn.close() 




# def get_location_by_product_svc(product_name):
#     conn = get_db_connection()
#     try:
#         status, result = get_location_by_product_repo(
#             conn, product_name)
#         # Check if data exists
#         if not result:
#             return False, "Invalid product"
        
#         return status, result
#     # Raise exception if failed
#     except Exception:
#         conn.rollback()
#         traceback.print_exc()
#         raise
#     finally:
#         conn.close() 


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

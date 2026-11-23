import traceback

from .query.prod_qry import (
    GET_PRODUCT_BY_LOCATION_ZONE_BIN,
    GET_LOCATION_BY_PRODUCT,
    GET_ALL_PRODUCTS,
    GET_CUR_STOCK_BY_ID,
    IST_OUTBOUND,
    IST_INBOUND,
    IST_TXN_LOGS
)

from models.prod_model import (
    Product,
    All_Product,
    Stock_Level
)

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


# Stock transfer
def get_current_stock_by_id_repo(conn, location_id, product_barcode):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            GET_CUR_STOCK_BY_ID, 
            (
                location_id,
                product_barcode,
            ))

        # Setting model
        columns = [desc[0] for desc in cursor.description]
        stock_Level = [Stock_Level.from_row(columns, row) for row in rows]

        return True, stock_Level
    finally:
        cursor.close()


def ist_outbound_repo(conn, quantity, product_id, location_id):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            IST_OUTBOUND, 
            (
                quantity,
                product_id,
                location_id
            ))

        if cursor.rowcount > 0:
            return True
        return False
    finally:
        cursor.close()


def ist_inbound_repo(conn, quantity, product_id, location_id, bin_id):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            IST_INBOUND, 
            (
                product_id,
                location_id,
                quantity,
                bin_id
            ))

        if cursor.rowcount > 0:
            return True
        return False
    finally:
        cursor.close()


def ist_txn_logs_repo(
        conn, 
        types, 
        product_id, 
        from_location_id, 
        to_location_id, 
        quantity, 
        reference, 
        note,
        user_id
    ):
    cursor = conn.cursor()
    try:
        # Execute query
        rows = cursor.execute(
            IST_TXN_LOGS, 
            (
                types, 
                product_id, 
                from_location_id, 
                to_location_id, 
                quantity, 
                reference, 
                note,
                user_id
            ))

        if cursor.rowcount > 0:
            return True
        return False
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

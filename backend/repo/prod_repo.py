from database.db import get_db_connection
from .query.prod_qry import GET_PRODUCT_BY_LOCATION, GET_LOCATION_BY_PRODUCT
from models.prod_model import Product

def get_product_by_location(location):
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute(GET_PRODUCT_BY_LOCATION, (location,))

    products = [
        Product(
            location = row[0], 
            sku = row[1], 
            barcode = row[2],
            name = row[3], 
            category = row[4], 
            unit = row[5], 
            reorder_level = row[6], 
            quantity = row[7]
        )
        for row in rows
    ]

    cursor.close()
    conn.close()

    return products

def get_location_by_product(product_name):
    conn = get_db_connection()
    cursor = conn.cursor()

    rows = cursor.execute(GET_LOCATION_BY_PRODUCT, (product_name,))

    products = [
        Product(
            location = row[0], 
            sku = row[1], 
            barcode = row[2],
            name = row[3], 
            category = row[4], 
            unit = row[5], 
            reorder_level = row[6], 
            quantity = row[7]
        )
        for row in rows
    ]

    cursor.close()
    conn.close()

    return products
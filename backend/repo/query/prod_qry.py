GET_PRODUCT_BY_LOCATION = """
    SELECT 
        l.name location, 
        p.sku, 
        p.barcode, 
        p.name, 
        p.category, 
        p.unit, 
        p.reorder_level, 
        s.quantity 
    FROM 
        locations l, 
        stock_levels s, 
        products p
    WHERE 
        l.id = s.location_id
    AND 
        s.product_id = p.id
    AND 
        l.name ILIKE %s;
"""

GET_PRODUCT_SUMMARY = """
    SELECT 
        l.name location, 
        p.sku, 
        p.barcode, 
        p.name, 
        p.category, 
        p.unit, 
        p.reorder_level, 
        s.quantity
    FROM 
        locations l, 
        stock_levels s, 
        products p
    WHERE 
        l.id = s.location_id
    AND 
        s.product_id = p.id
    AND 
        p.name ILIKE %s;
"""
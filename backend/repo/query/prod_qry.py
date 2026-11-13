GET_PRODUCT_BY_LOCATION = """
    SELECT 
        p.*, 
        s.quantity, 
        l.name location
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

GET_LOCATION_BY_PRODUCT = """
    SELECT 
        p.*, 
        s.quantity,
        l.name location
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

GET_ALL_BINS = """
    SELECT 
        l.name location, 
        l.code location_code, 
        z.code zone, 
        b.id bins
    FROM 
        locations l,
        zones z,
        bins b
    WHERE 
        l.id = z.location_id
    AND
        z.id = b.zone_id
    ;
"""

GET_ALL_BINS_BY_LOCATION = """
    SELECT 
        l.name location, 
        l.code location_code, 
        z.code zone, 
        b.id bins
    FROM 
        locations l,
        zones z,
        bins b
    WHERE 
        l.id = z.location_id
    AND
        z.id = b.zone_id
    AND
        l.name ILIKE %s
    ;
"""
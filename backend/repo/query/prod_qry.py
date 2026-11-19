GET_PRODUCT_BY_LOCATION_BIN = """
    SELECT 
		p.id, 
        p.barcode, 
        p.name, 
        p.category, 
        p.unit, 
        p.reorder_level, 
        COUNT(p.id) quantity,
		l.code location,
		z.id zone,
		b.id bin
    FROM 
        locations l,
        zones z,
        bins b,
		stock_levels st,
		products p
    WHERE 
        l.id = z.location_id
    AND
        z.id = b.zone_id
	AND
		st.location_id = l.id
	AND
		st.product_id = p.id
    AND 
        l.code = 'WH-001'
    AND
        z.id = 7
	GROUP BY
		p.id,
		l.code,
		z.id,
		b.id
	ORDER BY
		p.name
    ;
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


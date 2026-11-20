GET_PRODUCT_BY_LOCATION_ZONE_BIN = """
    SELECT  
        p.barcode, 
		p.sku,
        p.name, 
        p.category, 
        p.unit, 
        p.reorder_level,
		st.quantity quantity,
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
		st.product_id = p.barcode
    AND 
        l.code = %s
    AND
        z.id = %s
	AND
		b.id = %s
	GROUP BY
		p.barcode,
		st.quantity,
		l.code,
		z.id,
		b.id
	ORDER BY
		p.name
    ;
"""

GET_CUR_STOCK_BY_ID = """
    SELECT 
        st.*
    FROM 
        stock_levels st, 
        products p, 
        locations l
    WHERE 
        st.product_id = p.barcode
    AND 
        st.location_id = l.id
    AND 
        l.code = 'WH-001'
    AND 
        p.barcode = '97'
    FOR UPDATE OF st
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


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



# ============= Stock Transfer queries ==============

# Check and lock current stock
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
        l.id = %s
    AND 
        p.barcode = %s
    FOR UPDATE OF st
    ;
"""

# Deduction of stocks from source location
INS_OUTBOUND = """
    UPDATE 
        stock_levels
    SET 
        quantity = quantity - %s
    WHERE 
        product_id = %s
    AND 
        location_id = %s
    ;
"""

# Insertion od stocks to  destination location
INS_INBOUND = """
    INSERT INTO stock_levels (
    product_id,
    location_id,
    quantity,
	bin_id
    )
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (product_id, location_id)
    DO UPDATE SET
        quantity = stock_levels.quantity + EXCLUDED.quantity,
        bin_id = EXCLUDED.bin_id;
"""

# Update logs
INSERT_TRX_LOGS = """
    INSERT INTO transactions (
        type,
        product_id,
        from_location_id,
        to_location_id,
        quantity,
        reference,
        note,
        submission_id,
        user_id,
        created_at
    )
    VALUES (
        # 'TRANSFER',
        # 97,
        # 7,
        # 8,
        # 5,
        # 'Please parse ref from frontend here!', 
        # 'Please parse note from frontend here!',
        # gen_random_uuid(),
        # 28,
        # '2026-11-20 14:30:00'
        %s,
        %s,
        %s,
        %s,
        %s,
        %s, 
        %s,
        gen_random_uuid(),
        %s,
        %s
    );
"""
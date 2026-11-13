GET_ALL_LOCATIONS = """
    SELECT 
        l.id,
        l.code location_code, 
        l.name name,
        l.is_active,
        l.description,
        l.address address, 
        COUNT(DISTINCT z.code) zone_count, 
        COUNT(DISTINCT b.id) bin_count
    FROM 
        locations l,
        zones z,
        bins b
    WHERE 
        l.id = z.location_id
    AND
        z.id = b.zone_id
    GROUP BY 
        l.id, l.name, l.code, l.address
    ORDER BY 
        l.code
    ;
"""
GET_LOC_EXIST = """
    SELECT EXISTS (
        SELECT 
            1
        FROM 
            locations
        WHERE 
            code = %s
    ) AS location_exists;
"""

GET_ZONE_BY_LOC = """
    SELECT
        DISTINCT z.code zone,
        l.code location
    FROM
        locations l,
        zones z
    WHERE
        l.id = z.location_id
    AND
        l.code = %s
    ;
"""

GET_ALL_BINS = """
    SELECT 
        l.name location, 
        l.code location_code, 
        z.code zone, 
        b.id bin_id
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
        b.id bin_id
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


GET_LOCATIONS = """
    SELECT * FROM locations;
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


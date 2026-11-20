IST_USR_QRY = """
    INSERT INTO users (
        username, 
        full_name, 
        password_hash, 
        is_active, 
        created_at, 
        role
    ) 
    VALUES (
        %s,     
        %s,     
        %s,     
        %s,     
        %s,     
        %s      
    )
    RETURNING 
        id;
"""

SEL_USR_BY_NAME = """
    SELECT 
        * 
    FROM 
        users 
    WHERE 
        username = %s;  
"""
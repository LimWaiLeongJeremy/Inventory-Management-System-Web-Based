IST_USER_QRY = """
    INSERT INTO users (
        username, 
        full_name, 
        password_hash, 
        is_active, 
        created_at, 
        role
    ) 
    VALUES (
        %s,     #username
        %s,     #fullname
        %s,     #hashed Password
        %s,     #is_active
        %s,     #created_at
        %s      #role
    );
"""
from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import create_access_token


cred = {

    "id": "0",
    "username": "",
    "password": "",
    "role": "",
}


def user_create_svc(username, password):

    # Validate if user in DB
    if cred["username"]:
        # if user exist, return "user exist"
        return False, "User already registered"   

    # Encrypt the password
    # Using bcrypt to hash the password
    # and adding a salt for security and if more than one user have the same password the encrypted password will be different
    hashed_password = hashpw(
                        password.encode('utf-8'), 
                        gensalt()
    )

    # TODO
    # ist to db
    try:
        # If username don't exist, insert user with hash pw
        cred["username"] = username
        cred["password"] = hashed_password
        cred["role"] = "admin"
        
        return True, {
            "id": cred["id"],
            "username": cred["username"],
            "role": cred["role"]
        }
    # Raise exception if user creation failed
    except Exception:
        print("Failed to create user")
        raise 
    

    
def user_auth_svc(username, password):
    # TODO
    # qry db for use details

    # Check if user exists
    if cred["username"] == username:
        if checkpw(password.encode('utf-8'), cred['password']):
            access_token = create_access_token(
                                identity = cred['id'],
                                additional_claims={"role": cred['role']}
            )
            return True, access_token
        return False, "Invalid credentials"
    return False, "Invalid credentials"

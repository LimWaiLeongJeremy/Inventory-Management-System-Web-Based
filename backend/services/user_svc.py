from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import create_access_token
from repo.user_repo import ist_usr_repo, get_user_by_username


def user_create_svc(username, fullname, password, role):

    # Validate if user in DB
    # TODO 
    # velidate user in db

    # if cred["username"]:
    #     # if user exist, return "user exist"
    #     return False, "User already registered"   

    # Encrypt the password
    # Using bcrypt to hash the password
    # and adding a salt for security and if more than one user have the same password the encrypted password will be different
    hashed_password = hashpw(
                        password.encode('utf-8'), 
                        gensalt()
    ).decode('utf-8')

    try:
        status, result = ist_usr_repo(
            username, 
            fullname, 
            hashed_password, 
            role
        )
        if status:
            return True, {
                "employee_id": result
            }

    # Raise exception if user creation failed
    except Exception:
        print("Failed to create user")
        raise 
    

    
def user_auth_svc(username, password):
    try: 
        status, result = get_user_by_username(
            username
        )

        # Check if user exists
        if not result:
            return False, "Invalid credentials"

        # Check if password match
        if checkpw(password.encode('utf-8'), result['password_hash'].encode('utf-8')):
            # Create token
            access_token = create_access_token(
                                identity = str(result['id']),
                                additional_claims={"role": result['role']}
            )

            return True, access_token

       # Raise exception if user creation failed
    except Exception:
        print("Failed to find user")
        raise 

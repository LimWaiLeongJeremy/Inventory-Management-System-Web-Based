import traceback

from bcrypt import hashpw, gensalt, checkpw
from flask_jwt_extended import create_access_token
from repo.user_repo import ist_usr_repo, get_user_by_username

# Used to check the password when the user does not exist,
# so a wrong username takes as long as a wrong password
DUMMY_HASH = hashpw(b"dummy-password", gensalt())


def user_create_svc(username, fullname, password, role):

    try: 
        # Validate if user in DB
        status, result = get_user_by_username(
            username
        )

        # Check if user exists, else create user
        if not result:
            # Encrypt the password
            # Using bcrypt to hash the password
            # and adding a salt for security if more than one user have the same password the encrypted password will be different
            # .decode('utf-8') turns password into a plain string for storing
            hashed_password = hashpw(
                    password.encode('utf-8'), 
                    gensalt()
            ).decode('utf-8')

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

        return False, "User already registered"   

       # Raise exception if user creation failed
    except Exception:
        traceback.print_exc()
        raise 

    

    
def user_auth_svc(username, password):
    try: 
        status, result = get_user_by_username(
            username
        )

        # Check if user exists
        # still run checkpw so the response time does not reveal the username exists
        if not result:
            checkpw(password.encode('utf-8'), DUMMY_HASH)
            return False, "Invalid credentials"

        # Check if password match
        password_ok = checkpw(password.encode('utf-8'), result.password_hash.encode('utf-8'))

        # Same message for every failure so it does not reveal which part was wrong
        if not password_ok or not result.is_active:
            return False, "Invalid credentials"

        # Create token
        access_token = create_access_token(
                            identity = str(result.id),
                            additional_claims={"role": result.role}
        )

        return True, access_token

       # Raise exception if user creation failed
    except Exception:
        traceback.print_exc()
        raise 

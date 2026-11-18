from functools import wraps
from flask import session, redirect, url_for

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("route.login"))

        return func(*args, **kwargs)
    return wrapper
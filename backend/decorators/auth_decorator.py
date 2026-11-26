from functools import wraps
from flask import session, redirect, url_for

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("route.login"))

        return func(*args, **kwargs)
    return wrapper


# Only lets the listed roles open the page; everyone else goes back to the dashboard.
# Use it under @require_login, e.g.
#   @route_bp.route('/stocktaking')
#   @require_login
#   @require_role("supervisor")
def require_role(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if session.get("role") not in roles:
                return redirect(url_for("route.dashboard"))

            return func(*args, **kwargs)
        return wrapper
    return decorator

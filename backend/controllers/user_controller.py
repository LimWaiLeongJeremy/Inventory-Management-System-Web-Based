from flask import Blueprint, jsonify, request
from services.user_svc import user_create_svc


# ========== Create blueprint ==========
user_bp = Blueprint("auth", __name__)


# User API
@user_bp.route('/api/user/create', methods=['POST'])
def user_create_api():

    # get data from body
    data = request.get_json()  

    # Validate if body has content
    if data is None:
        return jsonify({
            "status": "error",
            "data": "Invalid or missing JSON data"
        }), 400

    # data sanitization
    username = data.get('username', "")
    password = data.get('password', "")
    
    # validate json value
    if not isinstance(username, str) or not username:
        return jsonify({
            "status": "error",
            "data": "Username cannot be empty"
        }), 400
    
    username = username.strip().lower()

    if not isinstance(password, str) or not password:
        return jsonify({
            "status": "error",
            "data": "Password cannot be empty"
        }), 400

    # Try to create user 
    try:
        success, result = user_create_svc(username, password)
        
        if not success:
            return jsonify({
                "status": "error",
                "data": result
            }),409
            
        return jsonify({
            "status": "success",
            "data": result
        }), 200   

    except Exception:
        import traceback
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500




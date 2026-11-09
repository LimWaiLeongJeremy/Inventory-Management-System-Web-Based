import traceback 
from flask import Blueprint, jsonify

from services.loc_svc import get_locations_svc


# ========== Create blueprint ==========
location_bp = Blueprint("location", __name__)



# location API
@location_bp.route('/api/location', methods=['GET'])
def getAllLoc():
    try:
        success, locations = get_locations_svc()

        if not success:
                return jsonify({
                    "status": "error",
                    "data": locations
                }),409

        return jsonify({
            "status": "success",
            "locations": locations
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500
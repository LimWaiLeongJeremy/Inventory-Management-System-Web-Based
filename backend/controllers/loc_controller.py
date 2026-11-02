from flask import Blueprint, jsonify

from services.loc_svc import get_locations_svc


# ========== Create blueprint ==========
location_bp = Blueprint("location", __name__)



# location API
@location_bp.route('/api/location', methods=['GET'])
def getAllLoc():

    locations = get_locations_svc()

    return jsonify({
        "status": "success",
        "data": locations
    }), 200
import traceback 

from flask import Blueprint, jsonify

from services.loc_svc import get_locations_svc, get_zone_by_loc_svc, get_loc_exist_svc, get_bin_by_zone_svc
from flask_jwt_extended import jwt_required

# ========== Create blueprint ==========
location_bp = Blueprint("location", __name__)


# location API
@location_bp.route('/api/location', methods=['GET'])
@jwt_required()
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
            "locations": [loc.to_dict() for loc in locations]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500


@location_bp.route('/api/<string:location_code>/zone', methods=['GET'])
@jwt_required()
def getZoneByLoc(location_code):

     # validate json value
    if not isinstance(location_code, str) or not location_code:
        return jsonify({
            "status": "error",
            "data": "location cannot be empty"
        }), 400
    
    try:
        exists = get_loc_exist_svc(location_code)
        if not exists:
            return jsonify({
                    "status": "error",
                    "data": "Location cannot be found"
                }),404

        success, zones = get_zone_by_loc_svc(location_code)

        if not success:
                return jsonify({
                    "status": "error",
                    "data": zones
                }),409

        return jsonify({
            "status": "success",
            "locations": [loc.to_dict() for loc in zones]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500

@location_bp.route('/api/<string:location_code>/<int:zone_id>', methods=['GET'])
@jwt_required()
def getBinByZone(location_code, zone_id):

    # validate json value
    if not isinstance(location_code, str) or not location_code:
        return jsonify({
            "status": "error",
            "data": "location cannot be empty"
        }), 400

    if not isinstance(zone_id, int) or not zone_id:
        return jsonify({
            "status": "error",
            "data": "zone cannot be empty"
        }), 400
        
    try:
        success, bins = get_bin_by_zone_svc(
            location_code, 
            zone_id
        )

        if not success:
                return jsonify({
                    "status": "error",
                    "data": bins
                }),409

        return jsonify({
            "status": "success",
            "locations": [loc.to_dict() for loc in bins]
        }), 200

    except Exception:
        traceback.print_exc()

        return jsonify({
            "status": "error",
            "data": "Internal server error"
        }), 500
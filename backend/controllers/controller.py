from datetime import datetime,timezone
from flask import Blueprint, jsonify


# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)


# ========== API ==========
# Heartbeat
@product_bp.route('/api/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "Iventeroy-app"
    }), 200


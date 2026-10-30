import model

from datetime import timezone
from datetime import datetime

from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ========== Routing frontend ==========
@app.route('/')
@app.route('/index.html')
@app.route('/home')
def home():
    return render_template('index.html')


# ========== API ==========
# Heartbeat
@app.route('/api/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({
        "status": "alive",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "service": "Iventeroy-app"
    }), 200

# location API
@app.route('/api/location', methods=['GET'])
def getAllLocation():

    # query location 
    locations = [
        {
            'location_id': loc['location_id'],
            'location_name': loc['location_name'],
            'description': loc['description']
        }
        for loc in model.location 
    ]

    return jsonify({
        "status": "success",
        "data": locations
    }), 200


# product api
@app.route('/api/locations/<string:location_name>/products', methods=['GET'])
def getProductByLocation(location_name):

    loc = next(
        (loc for loc in model.location if loc['location_name'] == location_name),
        None
    )
    if loc is None:
        return jsonify({
            'status': 'error',
            'message': 'Location not found'
        }), 404

    return jsonify({
        'status': "success",
        'location': {
            'location_id': loc['location_id'],
            'location_name': loc['location_name']
        },
        'data': loc['product']
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)



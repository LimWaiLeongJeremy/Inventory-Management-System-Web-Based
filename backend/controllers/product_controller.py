from flask import Blueprint, jsonify

from models.model import location


# ========== Create blueprint ==========
product_bp = Blueprint("product", __name__)





# # location API
# @app.route('/api/location', methods=['GET'])
# def getAllLoc():

#     # query location 
#     locations = [
#         {
#             'location_id': loc['location_id'],
#             'location_name': loc['location_name'],
#             'description': loc['description']
#         }
#         for loc in location 
#     ]

#     return jsonify({
#         "status": "success",
#         "data": locations
#     }), 200


# product api
@product_bp.route('/api/locations/<string:location_name>/products', methods=['GET'])
def getProdByLoc(location_name):

    loc = next(
        (loc for loc in location if loc['location_name'] == location_name),
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

# @product_bp.route('/api/product/summary', methods=['GET'])
# def getProdSum():
#     product_summary = {}

#     for loc in location:
#         for product in loc['product']:
#             product_id = product['product_id']

#             if product_id not in product_summary:
#                 product_summary[product_id] = {
#                     'product_id': product['product_id'],
#                     'sku': product['sku'],
#                     'name': product['name'],
#                     'category': product['category'],
#                     'unit': 0,
#                     'reorder_level': product['reorder_level'],
#                     'is_activve': product['is_active'],
#                     'create_at': product['create_at']
#                 }
#             product_summary[product_id]['unit'] += product['unit']

#     return jsonify({
#         'status': 'success',
#         'products': list(product_summary.values())
#     }), 200

# @product_bp.route('/api/products/<string:product_id>/locations', methods=['GET'])
# def getProLoc(product_id):
#     product_info = None
#     locations = []
#     total_quantity = 0

#     for loc in location: 
#         for product in loc['product']:
#             if product['product_id'] == product_id:
#                 if product_info is None:
#                     product_info = {
#                         'product_id': product['product_id'],
#                         'sku': product['sku'],
#                         'name': product['name']
#                     }
#                 locations.append({
#                     'location_id': loc['location_id'],
#                     'location_name': loc['location_name'],
#                     'quntity': product['unit']
#                 })
#                 total_quantity += product['unit']

#     if product_info is None: 
#         return jsonify({
#             'status': 'error',
#             'message': 'Product not found'
#         }), 404
    
#     return jsonify({
#         'status': 'success',
#         'data': {
#             **product_info,
#             'total_quantity': total_quantity,
#             'location': locations
#         }
#     }), 200

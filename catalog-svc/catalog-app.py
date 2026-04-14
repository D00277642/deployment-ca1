import os
FEATURE_DISCOUNT = os.getenv("FEATURE_DISCOUNT", "false")
from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/catalog', methods=['GET'])
def get_catalog():
    """Return all products from the catalog"""
    products = []
    # Redis keys are stored as 'product:1', 'product:2', etc.
    keys = r.keys('product:*')
    for key in keys:
        product_data = r.get(key)
        if product_data:
            product = json.loads(product_data)

            if FEATURE_DISCOUNT == "true":
                product["price"] = float(product["price"]) * 0.9

            products.append(product)

    return jsonify(products)

@app.route('/catalog', methods=['POST'])
def add_product():
    """Add a new product to the catalog"""
    product = request.json
    # Generate a new ID based on existing product count
    product_id = r.incr('next_product_id')
    product['id'] = product_id
    # Store the product with key 'product:<id>'
    r.set(f'product:{product_id}', json.dumps(product))
    return jsonify(product), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
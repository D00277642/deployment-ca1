from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    # Call the catalog service
    response = requests.get('http://catalog:5000/catalog')
    products = response.json()

    return render_template('shop-front.html.j2', products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
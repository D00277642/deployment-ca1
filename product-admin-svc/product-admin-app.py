from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('add-product.html.j2')

@app.route('/add-product', methods=['POST'])
def add_product():
    product_data = {
        'make': request.form['make'],
        'model': request.form['model'],
        'price': request.form['price']
    }
    
    # Send to catalog service
    response = requests.post('http://catalog:5000/add-product', json=product_data)
    
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Error adding product", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
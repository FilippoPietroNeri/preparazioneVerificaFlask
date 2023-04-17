import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
app = Flask(__name__)

df = pd.read_excel('https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true', sheet_name='products')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/es1')
def es1():
    listOfProducts = df.drop_duplicates(subset='category_id').sort_values(by='category_id')
    return render_template('es1.html', products=listOfProducts['category_id'])

@app.route('/es1/result', methods=['GET'])
def es1res(): 
    prodottoScelto = request.args.get('prodotto')

    result = df[int(prodottoScelto) == df.category_id].sort_values(by=["product_name"])
    return render_template('firstResults.html', products=result.to_html())

@app.route('/es2')
def es2():
    return render_template('es2.html')

@app.route('/es2/result', methods=['GET'])
def es2res(): 
    productMin = int(request.args.get('min'))
    productMax = int(request.args.get('max'))

    result = df[(df.list_price >= productMin) & (df.list_price <= productMax)].sort_values(by='list_price')
    return render_template('firstResults.html', products=result.to_html())

@app.route('/es3')
def es3():
    return render_template('es3.html')

@app.route('/es3/result', methods=['GET'])
def es3res(): 
    productName = request.args.get('product_name')

    result = df[df.product_name.str.contains(productName)].sort_values(by='product_name')
    return render_template('firstResults.html', products=result.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
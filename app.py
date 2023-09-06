from flask import Flask 
from crypto import client,symbol 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Binance API"
 
@app.route('/price', methods=['GET'])
def get_price():
    ticker = client.futures_symbol_ticker(symbol=symbol)
    crpto_price = float(ticker['price'])
    price = f"{crpto_price}"
    return price

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
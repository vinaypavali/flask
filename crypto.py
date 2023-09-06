import pandas as pd
from binance.client import Client

# Set up Binance Futures API
api_key ='gHEo2NxaZ2trJqpOqMTL68T7yj5KyY4w10UZ1qa31a3SwWWNlcHjUHyikmYL8F70'
api_secret = 'OPMCAFimgaQ6wWRZQzugN7f93Kb5baLBbeJJflhyApYWi3HJJ11KQ8rUJGWk0m56'

client = Client(api_key, api_secret)

# Define symbol and interval
symbol = 'COMPUSDT'
interval = Client.KLINE_INTERVAL_5MINUTE  
def data():
    # Retrieve klines data from Binance API
    klines = client.futures_historical_klines(
        symbol=symbol, # 'BTCUSDT' , 'COMPUSDT' , 'ETCUSDT' , 'LTCUSDT'
        interval=interval, #1MINUTE , 5MINUTE , #1HOUR , #1DAY
        start_str='2023-08-01'
    )

    df = pd.DataFrame(klines)
    df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'num_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')  # Convert timestamp to datetime format
    df = df.astype({'open': float, 'high': float, 'low': float, 'close': float, 'volume': float})  # Convert data types to float

    return df
import websocket
import json
import time

# List of symbols to track
symbols_to_track = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'ADAUSDT', 'DOTUSDT', 'XRPUSDT', 'DOGEUSDT', 'LINKUSDT', 'LTCUSDT', 'ALGOUSDT', 'MATICUSDT', 'XLMUSDT', 'VETUSDT', 'THETAUSDT', 'XEMUSDT', 'EOSUSDT', 'TRBUSDT']

# Dictionary to store live prices
live_prices = {symbol: None for symbol in symbols_to_track}

def on_open(ws):
    sub_msg = {"method": "SUBSCRIBE", "params": [f"{symbol.lower()}@ticker" for symbol in symbols_to_track], "id": 1}
    ws.send(json.dumps(sub_msg))

def on_message(ws, message):
    try:
        data = json.loads(message)
        if 's' in data and 'c' in data:
            symbol = data['s']
            if symbol.upper() in symbols_to_track:
                live_prices[symbol] = data['c']
                print_prices()
    except Exception as e:
        pass

def print_prices():
    # ANSI escape code for yellow color
    yellow_color_code = "\033[93m"
    # ANSI escape code for green color
    green_color_code = "\033[97m"
    # ANSI escape code to reset color
    reset_color_code = "\033[0m"

    # Move the cursor to the beginning of the line
    print('\r', end="")

    # Print live prices with yellow color, green letters, and reduced spacing
    prices_line = f"{'Live Price:': <15}|"
    letters = 'ABCDEFGHIJKLMNOPQ'

    for i, symbol in enumerate(symbols_to_track):
        price = live_prices.get(symbol, 'Error')
        letter = letters[i % len(letters)]
        prices_line += f"{green_color_code}{letter}{reset_color_code}{yellow_color_code}{price: <6}{reset_color_code}|"

    # Print the updated prices line
    print(prices_line, end="")

def on_error(ws, error):
    pass  # Ignore errors

def on_close(ws, close_status_code, close_msg):
    print(f"Closed with status code {close_status_code}. Reconnecting...")
    time.sleep(5)  # Wait for a few seconds before attempting to reconnect
    ws.run_forever()

url = "wss://fstream.binance.com/ws"

ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()

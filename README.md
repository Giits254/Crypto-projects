#Binance WebSocket Live Price Tracker
This script connects to Binance's WebSocket API to track live prices of selected cryptocurrency pairs. The prices are fetched in real-time and displayed in the terminal using colored output for better readability.

Features
Tracks live prices of multiple cryptocurrency pairs.
Displays live prices in the terminal with colored and labeled formatting.
Automatically reconnects in case of a connection drop.

#Getting Started
Prerequisites
Python 3.x
websocket-client library
You can install the required WebSocket library using pip:
pip install websocket-client

Running the Script
Clone the repository or copy the script to your local machine.
Ensure you have the required Python environment.

Run the script using Python:
python live_price_tracker.py

The script tracks a predefined list of symbols. You can customize the symbols by modifying the symbols_to_track list in the script.

How It Works
The script connects to Binance's futures WebSocket API.
On connection, it subscribes to ticker updates for the specified cryptocurrency pairs.
As live price updates are received, they are parsed and displayed in the terminal.
If the connection is lost, the script will attempt to reconnect automatically.
Customization
Symbols to Track: Modify the symbols_to_track list to include any other cryptocurrency pairs you are interested in.
Color and Format: Customize the print_prices() function to change the color scheme and format of the terminal output.
Error Handling
Basic error handling is included to ensure the script continues running even if unexpected data or connection issues occur.
License

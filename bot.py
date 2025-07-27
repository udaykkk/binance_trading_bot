from binance.client import Client
from dotenv import load_dotenv
import os
import logging
import traceback
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


logging.basicConfig(
    filename='bot.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class BasicBot:
    def __init__(self, api_key=API_KEY, api_secret=API_SECRET, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        logging.info(" Connected to Binance Futures Testnet")

    def log_and_return(self, action, result):
        logging.info(f"{action} Success: {result}")
        return result

    def log_and_error(self, action, error):
        logging.error(f"{action} Failed: {str(error)}\n{traceback.format_exc()}")
        return f"{action} Failed: {str(error)}"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            return self.log_and_return("Market Order", order)
        except Exception as e:
            return self.log_and_error("Market Order", e)

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            return self.log_and_return("Limit Order", order)
        except Exception as e:
            return self.log_and_error("Limit Order", e)

    def place_stop_market_order(self, symbol, side, quantity, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=stop_price,
                quantity=quantity,
                timeInForce="GTC"
            )
            return self.log_and_return("Stop-Market Order", order)
        except Exception as e:
            return self.log_and_error("Stop-Market Order", e)

#  Binance Futures Trading Bot (Python)

A simple Python command-line trading bot to execute **MARKET**, **LIMIT**, and **STOP_MARKET** orders on the **Binance Futures Testnet**.


---

##  Features

-  Supports `MARKET`, `LIMIT`, `STOP_MARKET` order types  
-  Built using `python-binance`, `dotenv`, `argparse`  
-  Secure `.env` credential loading  
-  Logging enabled to `bot.log`  
-  Easily extendable for additional order types  



## Project Structure
binance_trading_bot/
├── bot.py # Bot logic & order placement
├── cli.py # Command-line interface
├── bot.log # Order logs
├── requirements.txt # Python package requirements
└── demo.png # Demo image 


---

## 🧪 Binance Testnet API Setup

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)  
2. Register / log in  
3. Generate **API Key & Secret**
4. Make sure to **enable Futures permission** (checkbox)  
5. Add the credentials to `.env`:


---

## 💻 Installation & Setup

```bash
# 1. Clone this repo
git clone https://github.com/your-username/binance_trading_bot.git
cd binance_trading_bot

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a command
python cli.py --type MARKET --symbol BTCUSDT --side BUY --quantity 0.002



 Example Commands

# Market Order
python cli.py --type MARKET --symbol BTCUSDT --side BUY --quantity 0.002

# Limit Order
python cli.py --type LIMIT --symbol BTCUSDT --side SELL --quantity 0.002 --price 71000

# Stop-Market Order
python cli.py --type STOP_MARKET --symbol BTCUSDT --side SELL --quantity 0.002 --stop_price 

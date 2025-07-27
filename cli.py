import argparse
from bot import BasicBot

def valid_symbol(symbol):
    return symbol.upper()

def valid_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise argparse.ArgumentTypeError("Side must be BUY or SELL.")
    return side

def main():
    parser = argparse.ArgumentParser(description="Crypto Trading Bot CLI")

    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_MARKET"], help="Order type")
    parser.add_argument("--symbol", required=True, type=valid_symbol, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, type=valid_side, help="BUY or SELL")
    parser.add_argument("--quantity", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Limit price (for LIMIT)")
    parser.add_argument("--stop_price", type=float, help="Stop price (for STOP_MARKET)")

    args = parser.parse_args()
    bot = BasicBot()

    try:
        if args.type == "MARKET":
            result = bot.place_market_order(args.symbol, args.side, args.quantity)

        elif args.type == "LIMIT":
            if not args.price:
                print(" Error: --price is required for LIMIT order.")
                return
            result = bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)

        elif args.type == "STOP_MARKET":
            if not args.stop_price:
                print(" Error: --stop_price is required for STOP_MARKET order.")
                return
            result = bot.place_stop_market_order(args.symbol, args.side, args.quantity, args.stop_price)

        else:
            print(" Invalid order type selected.")
            return

        print(" Order Result:")
        print(result)

    except Exception as e:
        print(" Exception occurred during order placement:")
        print(str(e))

if __name__ == "__main__":
    main()

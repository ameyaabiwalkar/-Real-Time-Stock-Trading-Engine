import threading
import time
import random

# Atomic counter for unique order ID generation
class AtomicInteger:
    def __init__(self, initial=0):
        self.value = initial
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1
            return self.value

# Stock Order Book Class with Lock-Free Concept
class StockOrderBook:
    def __init__(self):
        self.buy_orders = []  # Using a list instead of deque
        self.sell_orders = []  # Using a list instead of deque
        self.order_id_generator = AtomicInteger()  # Atomic integer for order ID

    def addOrder(self, order_type, ticker, quantity, price):
        
        order_id = self.order_id_generator.increment()
        new_order = (ticker, quantity, price, order_type, order_id)

        # Add order to buy or sell list
        if order_type == "Buy":
            self.buy_orders.append(new_order)
            self.sortOrders(self.buy_orders, is_buy=True)  # Sort descending for Buy orders
        else:
            self.sell_orders.append(new_order)
            self.sortOrders(self.sell_orders, is_buy=False)  # Sort ascending for Sell orders

        print(f"Added {order_type} order: {ticker} {quantity} @ ${price}")
        self.matchOrder()

    def sortOrders(self, orders, is_buy):
        # Efficient sorting with the sort method (since we're using lists)
        orders.sort(key=lambda x: x[2], reverse=is_buy)  # For Buy: descending; For Sell: ascending

    def matchOrder(self):
        i, j = 0, 0
        while i < len(self.buy_orders) and j < len(self.sell_orders):
            buy_ticker, buy_quantity, buy_price, _, _ = self.buy_orders[i]
            sell_ticker, sell_quantity, sell_price, _, _ = self.sell_orders[j]

            if buy_ticker == sell_ticker and buy_price >= sell_price:  # If Match is found
                matched_quantity = min(buy_quantity, sell_quantity)
                print(f"Matched {matched_quantity} shares of {buy_ticker} at ${sell_price}")

                if buy_quantity > matched_quantity:
                    self.buy_orders[i] = (buy_ticker, buy_quantity - matched_quantity, buy_price, "Buy", self.buy_orders[i][4])
                else:
                    i += 1  # Remove buy order

                if sell_quantity > matched_quantity:
                    self.sell_orders[j] = (sell_ticker, sell_quantity - matched_quantity, sell_price, "Sell", self.sell_orders[j][4])
                else:
                    j += 1  # Remove sell order

            else:
                break  

        # Remove fully matched orders
        self.buy_orders = self.buy_orders[i:]
        self.sell_orders = self.sell_orders[j:]

# Simulating Random Stock Trading
def simulate_trading(order_book):
    tickers = ["AAPL", "GOOGL", "TSLA", "AMZN", "MSFT"]
    while True:
        order_type = random.choice(["Buy", "Sell"])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 10)
        price = random.randint(100, 500)

        order_book.addOrder(order_type, ticker, quantity, price)
        time.sleep(random.uniform(0.5, 1.5))  # Simulating delay

if __name__ == "__main__":
    stock_order_book = StockOrderBook()
    trading_thread = threading.Thread(target=simulate_trading, args=(stock_order_book,))
    trading_thread.start()

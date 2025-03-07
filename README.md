# Real-Time Stock Trading Engine

This project implements a real-time stock trading engine designed to match Buy and Sell orders efficiently, using a simulated multi-threaded environment. It supports up to 1,024 different stock tickers and handles stock transactions with concurrency, ensuring thread safety for real-time stock trading scenarios. The system matches Buy and Sell orders based on specific criteria and processes orders using a lock-free mechanism, utilizing atomic operations for order ID generation and avoiding the use of dictionaries or maps.

## Requirements

- Python 3.x
- `threading`, `time`, and `random` standard libraries

### Functional Requirements

1. **`addOrder` function**:
    - Parameters: 
        - `order_type`: Type of order ("Buy" or "Sell")
        - `ticker`: Ticker symbol of the stock (e.g., AAPL, GOOGL)
        - `quantity`: Quantity of stocks to buy or sell
        - `price`: Price at which the stock is to be bought or sold
    - Supports adding Buy or Sell orders.
    - Handles up to 1,024 stock tickers being traded.
    - Orders are added to a central order book and sorted based on the type (Buy orders are sorted in descending price order, Sell orders in ascending price order).
    - Randomly executed trades simulate active stock transactions using different parameter values.

2. **`matchOrder` function**:
    - Matches Buy and Sell orders using the following criteria:
        - The Buy price must be greater than or equal to the Sell price for matching orders.
        - The matching process ensures that the orders are processed in an efficient manner with a time complexity of **O(n)**, where `n` is the number of orders in the order book.
        - When a match is found, the orders are updated with the matched quantity, and fully matched orders are removed from the order book.

3. **Concurrency Handling**:
    - The system simulates a multi-threaded environment where multiple stock orders are processed concurrently.
    - Thread safety is achieved using Python's `threading.Lock` to prevent race conditions when modifying the order book.

4. **Lock-Free Data Structures**:
    - The order book utilizes lists instead of dictionaries, avoiding the use of maps or equivalent data structures. Sorting of the orders is done manually using the `sort()` method.
    - The `AtomicInteger` class is used to generate unique order IDs in a thread-safe manner without using locks on the order book.

## Features

- **Real-Time Order Matching**: The engine simulates real-time matching of Buy and Sell orders.
- **Concurrency**: Multiple threads simulate active stock trading in a multi-threaded environment.
- **Atomic Order ID Generation**: Unique order IDs are generated atomically, ensuring that each order has a unique identifier.
- **Efficient Sorting**: Buy orders are sorted in descending order by price, and Sell orders are sorted in ascending order.
- **Simulated Trading**: Random orders are generated with varying prices and quantities to simulate active stock trading.

## Instructions

### 1. Clone the Repository


git clone https://github.com/ameyaabiwalkar/Real-Time-Stock-Trading-Engine.git
cd stock-trading-engine

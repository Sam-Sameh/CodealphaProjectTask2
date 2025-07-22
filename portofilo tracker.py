# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 145
}

def stock_tracker():
    total_value = 0
    portfolio = {}

    print("📈 Welcome to the Stock Portfolio Tracker!")
    print("Type 'done' when finished.\n")

    while True:
        stock = input("Enter stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❌ Stock not found in database.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
            portfolio[stock] = quantity
            total_value += stock_prices[stock] * quantity
        except ValueError:
            print("❌ Please enter a valid number.")

    print("\n💼 Your Investment Summary:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        print(f"- {stock}: {qty} shares x ${price} = ${qty * price}")

    print(f"\n💰 Total Investment Value: ${total_value}")

    # Optional: Save to file
    save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
    if save == "yes":
        with open("portfolio_summary.txt", "w") as file:
            file.write("Stock Portfolio Summary:\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                file.write(f"{stock}: {qty} shares x ${price} = ${qty * price}\n")
            file.write(f"\nTotal Investment Value: ${total_value}\n")
        print("✅ Summary saved to 'portfolio_summary.txt'.")

# Run the tracker
stock_tracker()

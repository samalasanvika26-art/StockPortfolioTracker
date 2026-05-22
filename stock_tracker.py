# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

# Taking user input
for i in range(n):
    stock_name = input("Enter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        portfolio[stock_name] = quantity
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
    else:
        print("Stock not available.")

# Display portfolio details
print("\nPortfolio Summary")
print("-------------------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity

    print(f"{stock} - Quantity: {quantity}, Price: ${price}, Total: ${investment}")

print("\nTotal Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(f"{stock} - Quantity: {quantity}, Price: ${price}, Total: ${investment}\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved to portfolio.txt")
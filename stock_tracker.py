import datetime

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📊 Welcome to Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("⚠️ Quantity must be positive!")
            continue
    except ValueError:
        print("⚠️ Enter a valid number!")
        continue

    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    # Store in portfolio
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"✅ {stock} added! Investment: {investment}")

# 📊 Display Portfolio Summary
print("\n📊 Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    print(f"{stock} - Quantity: {qty}, Price: {price}, Total: {qty * price}")

print("\n💰 Total Investment:", total_investment)

# 💾 Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write(f"Date: {datetime.datetime.now()}\n\n")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        file.write(f"{stock} - Qty: {qty}, Price: {price}, Total: {qty * price}\n")

    file.write(f"\nTotal Investment: {total_investment}")

print("\n📁 Portfolio saved to 'portfolio.txt'")
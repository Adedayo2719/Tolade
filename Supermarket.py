def calculate_profit_or_loss(cost_price, selling_price):
    """
    Function to calculate profit or loss based on cost price and selling price.
    
    Args:
    - cost_price: Float, cost price of the item.
    - selling_price: Float, selling price of the item.
    
    Returns:
    - Float: Profit (if positive) or loss (if negative).
    """
    return selling_price - cost_price

# Data provided
items = {
    "Rice": {"cost_price": 800, "selling_price": 630},
    "Toothpaste": {"cost_price": 12, "selling_price": 20},
    "Diapers": {"cost_price": 100, "selling_price": 91},
    "Sponge": {"cost_price": 5, "selling_price": 10},
    "Egg": {"cost_price": 80, "selling_price": 73}
}

# Lists to track gains and losses
gains = []
losses = []
overall_profit = 0

# Calculate profits or losses for each item
for item, prices in items.items():
    cost_price = prices["cost_price"]
    selling_price = prices["selling_price"]
    profit_or_loss = calculate_profit_or_loss(cost_price, selling_price)
    
    if profit_or_loss > 0:
        gains.append((item, cost_price))
    elif profit_or_loss < 0:
        losses.append((item, cost_price))
    
    overall_profit += profit_or_loss

# Print profits
print("Items where you gained profit:")
for item, cost_price in gains:
    print(f"{item}: Cost Price = ${cost_price}")

print("\nItems where you incurred losses:")
for item, cost_price in losses:
    print(f"{item}: Cost Price = ${cost_price}")

# Print overall financial outcome
if overall_profit > 0:
    print(f"\nOverall, you gained a profit of ${overall_profit}.")
elif overall_profit < 0:
    print(f"\nOverall, you incurred a loss of ${abs(overall_profit)}.")
else:
    print("\nOverall, you broke even (no profit, no loss).")

prices = [29.99, 45.50, 12.75, 38.20]
discount1 = 0.10
discount2 = 0.20
discount3 = 0.15
discount4 = 0.05

for cost in range(len(prices)):
    if cost == 0:
        discount = discount1
    elif cost == 1:
        discount = discount2
    elif cost == 2:
        discount = discount3
    elif cost == 3:
        discount = discount4

    # ← Indented inside the for-loop
    prices[cost] -= prices[cost] * discount
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")

print("Updated Prices:", prices)
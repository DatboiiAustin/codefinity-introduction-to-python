produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

groceries = [produce, dairy]
print("Groceries")
for section in groceries:
    for item in section:
        print(f"Item name:", item)
    print("")
        
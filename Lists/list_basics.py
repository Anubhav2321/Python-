items = []

print("Enter 3 items: ")
for i in range(3):
    item = input(f"Item {i+1}: ")
    items.append(item)

print("Your list:", items)
print("First item:", items[0])

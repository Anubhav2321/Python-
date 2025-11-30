numbers = [10, 20, 30]

value = int(input("Enter a number to add: "))
numbers.append(value)

remove_val = int(input("Enter number to remove (10/20/30): "))
if remove_val in numbers:
    numbers.remove(remove_val)

print("Updated list:", numbers)

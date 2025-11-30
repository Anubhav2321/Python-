age = int(input("Enter age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes":
    print("You can vote ✔")
else:
    print("You cannot vote ❌")

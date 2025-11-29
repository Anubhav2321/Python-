# Coffee Shop Management System

class CoffeeShop:
    def __init__(self):
        self.menu = {
            "Cappuccino": 150,
            "Burger": 100,
            "Momo": 80,
            "idli": 120,
            "pizza": 130,
            "chicken pokora": 150
        }
        self.orders = []

    def show_menu(self):
        print("\n---- Coffee Shop Menu ----")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price}")
        print("-----------------------------")

    def take_order(self):
        while True:
            self.show_menu()
            choice = input("\nEnter the item you want.. (or 'q' to finish order): ").title()

            if choice == 'Q':
                break

            if choice in self.menu:
                try:
                    quantity = int(input("Enter quantity: "))
                    self.orders.append((choice, quantity, self.menu[choice] * quantity))
                    print(f"✅ Added {quantity} x {choice} to your order.\n")
                except ValueError:
                    print("❌ Please enter a valid number.")
            else:
                print("❌ Sorry, that item is not on the menu.")

    def show_bill(self):
        if not self.orders:
            print("\n🧾 No orders to display.")
            return

        print("\n---- 🧾 Your Bill ----")
        total = 0
        for item, quantity, price in self.orders:
            print(f"{item} x {quantity} = ₹{price}")
            total += price
        print("-----------------------")
        print(f"Total Amount: ₹{total}")
        print("Thank you for visiting our Coffee Shop! ☕")

# --------- Main Program ---------
def main():
    shop = CoffeeShop()
    while True:
        print("\n1. Show Menu")
        print("2. Take Order")
        print("3. Show Bill")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            shop.show_menu()
        elif choice == '2':
            shop.take_order()
        elif choice == '3':
            shop.show_bill()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

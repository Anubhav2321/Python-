class ATM:
    def __init__(self):
        self.user_pin = None
        self.balance = 0.0

    def setup_pin(self):
        while True:
            pin = input("Set your 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                confirm_pin = input("Confirm your PIN: ")
                if pin == confirm_pin:
                    self.user_pin = pin
                    print("PIN set successfully!\n")
                    break
                else:
                    print("PINs do not match. Try again.\n")
            else:
                print("Invalid PIN. PIN must be 4 digits.\n")

    def verify_pin(self):
        for _ in range(3):  # Allow max 3 attempts
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.user_pin:
                print("PIN verified successfully!\n")
                return True
            else:
                print("Incorrect PIN.\n")
        print("Too many failed attempts. Access Denied.\n")
        return False

    def display_menu(self):
        print("\n=== ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance:.2f}")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount:.2f} deposited successfully.")
            else:
                print("Enter a positive amount.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Enter a positive amount.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"₹{amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        print("==== Welcome to the Python ATM ====")
        self.setup_pin()

        if not self.verify_pin():
            return

        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# === Main Program ===
if __name__ == "__main__":
    atm = ATM()
    atm.run()

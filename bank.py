class Bank:
    def __init__(self):
        self.balance = 0

    def show_balance(self):
        print(f"\n✅ Your Balance is: ₹ {self.balance}\n")

    def withdraw(self):
        try:
            amount = int(input("Enter Amount to Withdraw: ₹"))
            if amount <= 0:
                print("❌ Withdrawal amount must be more than 100₹.\n")
            elif amount > self.balance:
                print("❌ Insufficient balance.\n")
            else:
                self.balance -= amount
                print(f"💸 ₹{amount} withdrawn successfully.\n")
        except ValueError:
            print("❌ Invalid input. Enter a valid amount.\n")

    def deposit(self):
        try:
            amount = int(input("Enter Amount to Deposit: ₹"))
            if amount <= 0:
                print("❌ Deposit amount must be positive.\n")
            else:
                self.balance += amount
                print(f"💰 ₹{amount} deposited successfully.\n")
        except ValueError:
            print("❌ Invalid input. Enter a valid amount.\n")


# Main Program
if __name__ == "__main__":
    b = Bank()

    while True:
        print("------ BANK MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            op = int(input("Enter your choice (1-4): "))
            match op:
                case 1:
                    b.show_balance()
                case 2:
                    b.deposit()
                case 3:
                    b.withdraw()
                case 4:
                    print("🙏 Thank you for using our service!")
                    break
                case _:
                    print("⚠️ Invalid option. Please select between 1-4.\n")
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

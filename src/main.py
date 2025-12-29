def show_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add transaction")
    print("2. View summary")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
    t_type = input("Enter type (income/expense): ").lower()
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    if t_type not in ["income", "expense"]:
        print("Invalid transaction type.")
        continue

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number.")
        continue

    with open("data.csv", "a") as file:
        file.write(f"{t_type},{amount},{category}\n")

    print("Transaction added successfully!")


        elif choice == "2":
    income = 0
    expense = 0

    try:
        with open("data.csv", "r") as file:
            next(file)  # skip header
            for line in file:
                t_type, amount, _ = line.strip().split(",")
                amount = float(amount)

                if t_type == "income":
                    income += amount
                elif t_type == "expense":
                    expense += amount

        balance = income - expense

        print("\n--- Financial Summary ---")
        print(f"Total Income: {income}")
        print(f"Total Expense: {expense}")
        print(f"Balance: {balance}")

    except FileNotFoundError:
        print("No data found. Add transactions first.")


        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

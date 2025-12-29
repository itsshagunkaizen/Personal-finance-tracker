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
            print("Add transaction feature coming soon...")
        elif choice == "2":
            print("Summary feature coming soon...")
        elif choice == "3":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

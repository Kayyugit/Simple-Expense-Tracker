import json

def add_expense(expenses, category, description, amount):
    expenses.append({"category": category, "description": description, "amount": amount})
    print(f"Added expense: {category} - {description}, Amount: {amount}")

def get_total_expenses(expenses):
    return sum(expense["amount"] for expense in expenses)

def get_balance(budget, expenses):
    return budget - get_total_expenses(expenses)

def show_budget_details(budget, expenses):
    print(f"Total Budget: {budget}")
    print(f"Expenses:")
    for expense in expenses:
        print(f"- {expense['category']} - {expense['description']}: {expense['amount']}")
    print(f"Total Spent: {get_total_expenses(expenses)}")
    print(f"Remaining Budget: {get_balance(budget, expenses)}")

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data["initial_budget"], data["expenses"]
    except (FileNotFoundError, json.JSONDecodeError):
        return 0, []  

def save_budget_details(filepath, initial_budget, expenses):
    data = {
        'initial_budget': initial_budget,
        'expenses': expenses
    }
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def budget_tracker():
    print("=" * 40) 
    print("EXPENSE TRACKER".center(40)) 
    print("=" * 40)

    print("This is a simple expense tracker that takes an initial amount.")
    print("Then, adding your expense, the amount is automatically subtracted from the total amount.")
    filepath = 'budget_data.json'
    initial_budget, expenses = load_budget_data(filepath)
    if initial_budget == 0:
        initial_budget = float(input("Please enter your initial budget: "))
    budget = initial_budget

    while True:
        print("........................................")
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show budget details")
        print("3. Add more money to the budget")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print("........................................")
            categories = ["Food", "Transport", "Entertainment", "Bills", "Others"]
            print("Choose a category for the expense:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            category_choice = int(input("Enter the category number: "))
            category = categories[category_choice - 1]
            description = input("Enter expense description: ").lower()
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, description, amount)
        elif choice == "2":
            print("........................................")
            show_budget_details(budget, expenses)
        elif choice == "3":
            print("........................................")
            additional_amount = float(input("Enter the amount to add to the budget: "))
            budget += additional_amount
            print(f"Added {additional_amount} to the budget. New amount: {budget}")
        elif choice == "4":
            print("........................................")
            save_budget_details(filepath, initial_budget, expenses)
            print("Exiting Expense Tracker....")
            break
        else:
            print("........................................")
            print("Invalid option, please choose a valid option.")
        
        remaining_balance = get_balance(budget, expenses)
        if remaining_balance < 0.2 * initial_budget:
            print("........................................")
            print("Warning: Your remaining balance is below 20% of your initial budget.")
            add_more = input("Would you like to add more money to your budget? (yes/no): ").lower()
            if add_more == "yes":
                print("........................................")
                additional_amount = float(input("Enter the amount to add to the budget: "))
                budget += additional_amount
                print(f"Added {additional_amount} to the budget. New amount: {budget}")

if __name__ == "__main__":
    budget_tracker()

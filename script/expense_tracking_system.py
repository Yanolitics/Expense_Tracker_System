author = "Yanolitics"

print(f"""
┌────────────────────────────────┐
│   EXPENSE TRACKING SYSTEM      │
│        by {author:<12}         │
└────────────────────────────────┘
""")

# -------------------------------------------------------------------
#Part 1: Database Simulation
# -------------------------------------------------------------------

expenses = []

# -------------------------------------------------------------------
#Part 2: Validation Functions
# -------------------------------------------------------------------

def add_expense(amount: float, category: str, description: str) -> dict:
    """Validate that amount is greater than 0 and create an expense entry."""
    if amount <= 0.0:
        raise ValueError("Amount must be greater than 0.0.")
    else:
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        expenses.append(expense)
        return expense

# -------------------------------------------------------------------
#Part 3: Calculate Total Expenses
# -------------------------------------------------------------------

def calculate_total_expenses() -> float:
    """Calculate the total amount of all expenses."""
    total_amount = sum(expense["amount"] for expense in expenses)
    return total_amount


# -------------------------------------------------------------------
#Part 4: Calculate Total by Category
# -------------------------------------------------------------------

def calculate_total_by_category(category) -> float:
    """Calculate the total amount of all expenses for a given category."""
    total_per_category = sum(expense["amount"] for expense in expenses if expense["category"].lower() == category.lower())
    return total_per_category

# -------------------------------------------------------------------
#Part 5: Show All Expenses
# -------------------------------------------------------------------

def show_expenses() -> None:
    """Display all recorded expenses with item numbers."""
    if not expenses:
        print("No expenses recorded.")
    else:
        print("All Recorded Expenses:")
        for item_number, expense in enumerate(expenses, start=1):
            print(f"{item_number}. {expense['category']} - {expense['description']} : ${expense['amount']:.2f}")
    print()

# -------------------------------------------------------------------
#Part 6: Running Tests
# -------------------------------------------------------------------

def run_tests():
    """Execute sample expense tracking scenarios."""
    test_expenses = [
        (100.0, "Food", "Lunch at restaurant"),
        (50.0, "Transport", "Taxi fare"),
        (-20.0, "Entertainment", "Movie ticket"),  # Invalid expense
        (200.0, "Food", "Grocery shopping"),
        (75.0, "Transport", "Bus pass")
    ]

    for index, (amount, category, description) in enumerate(test_expenses, start=1):
        print(f"\nTest {index}: Adding expense - Amount: {amount}, Category: {category}, Description: {description}")
        try:
            result = add_expense(amount, category, description)
            print("Expense added successfully:", result)
        except ValueError as error:
            print("Failed to add expense:", str(error))

    print("-"*50)
    total_expenses = calculate_total_expenses()
    print(f"\nTotal Expenses: {total_expenses}")
    print(f"Total Food Expenses: {calculate_total_by_category('Food')}\n")
    print("-"*50, "\n")

    show_expenses()
    print("-"*50, "\n")

if __name__ == "__main__":
    run_tests()

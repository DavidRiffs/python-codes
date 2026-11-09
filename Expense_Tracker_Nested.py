expenses = {
    "E1": {
        "description": "food",
        "category": "feeding",
        "amount": 25000
    },
    "E2": {
        "description": "transport_fare",
        "category": "transportation",
        "amount": 15000
    },
    "E3": {
        "description": "internet",
        "category": "bills",
        "amount": 5000
    }
}
def add_expense():
    description = input("Enter Discription: ").strip()
    category = input("Enter Category: ").strip()
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Please Enter A Valid Number.")
        expense_id = f"len(E({expenses}))+1"
        expenses[expense_id] = {
            f"description": "{description}",
            f"category": "{category}",
            f"amount": "{amount}"
        }
        print("Expense Added Successfully.")
def view_expenses():
    for items in expenses.items():
        print(items)
def search_expense():
    expense_id = input("Enter expense ID: ").strip().lower()
    if expense_id in expenses:
        print(expenses[expense_id])
        return
    print("Not Found")
def total_expense():
    total = sum({expense["amount"] for expense in expenses.values()})
    print(f"Total Expenses: {total}")
def highest_expense():
    highest = max(expenses, key=lambda sid: (expenses[sid]["amount"]))
    print(f"Highest Expense: {expenses[highest]["description"]} {expenses[highest]["category"]} {expenses[highest]["amount"]}")
def delete_expense():
    expense_id = input("Enter Expense ID: ").strip().lower()
    if expense_id in expenses:
        delete = input("Do You Want To Delete Expense?(yes/no): ")
        if delete == "yes":
            del expenses[expense_id]
            print("Expense Deleted Successfully.")
            return
        print("Error")
        return
    print("Not Found.")
def update_expense():
    expense_id = input("Enter Exense ID To Update: ").strip().lower()
    description = input("Enter Expense Description: ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    if expense_id in expenses:
        expenses[expense_id] = {
            f"description": {description},
            f"category": {category},
            f"amount": {amount}
        }
        print("Expense Updated Successfully.")
    else:
        print("Not Found")
def expense_summary():
    print("\n====EXPENSES SUMMARY====\n")
    for expense_id, expense in expenses.items():
        print(f"{expense_id}: {expense["category"]} {expense["amount"]}")
while True:
    print("\n=====EXPENSE TRACKER=====\n" \
        "1).Add Expense\n" \
        "2).View All Expenses\n" \
        "3).Search Expense\n" \
        "4).Calculate Total Expenses\n" \
        "5).Find Highest Expense\n" \
        "6).Delete Expense\n" \
        "7)Update Expense\n" \
        "8).Category summary\n" \
        "9).Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        total_expense()
    elif choice == "5":
        highest_expense()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        update_expense()
    elif choice == "8":
        expense_summary()
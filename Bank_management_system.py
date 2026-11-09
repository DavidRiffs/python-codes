customers ={
  "C001":{
    "name": "David",
    "age": 25,
    "balance": 150000,
    "transactions": []
  },
  "C002":{
    "name": "Daniel",
    "age": 30,
    "balance": 90000,
    "transactions": []
  },
  "C003": {
    "name": "Joe",
    "age": 28,
    "balance": 200000,
    "transaction": []
  }
}
from datetime import datetime
def log_transaction(customer, description):
    timestamp = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    customer["transaction"].append(f"{timestamp}-{description}")
def create_customer():
    name = input("Enter Name Of Customer: ")
    age = int(input("Enter Age Of Customer: "))
    balance = int(input("Enter Balance Of Customer: "))
    customer_id = f"C(len({customers}) + 1"
    customers[customer_id] = {
        f"name": {name},
        f"age": {age},
        f"balance": {balance},
        f"transaction": []
    }
def view_all_customers():
    for item in customers.items():
        print(item)
def search_customer():
    customer_id = input("Enter Customer ID: ").strip()
    if customer_id in customers:
        customer = customers[customer_id]
        print(f"ID Found: {customer}")
        #print(f"Name: {customer["name"]}")
        #print(f"{Age: customer["age"]}")
        #print(f"{Balance: customer["balance"]}")
        return
    print("Not Found.")
def Deposit_money():
    customer_id = input("Enter Customer ID: ").strip().title()
    if customer_id in customers:
        amount = float(input("Enter Amount To Deposit: "))
        customer = customers[customer_id]
        customer["balance"] += amount
        log_transaction(customer, f"Deposited {amount}")
        print(f"{amount} Deposited Successfully")
def withdraw_money():
    customer_id = input("Enter Customer ID: ").strip().title()
    if customer_id in customers:
        amount = float(input("Enter Amount To Withdraw: "))
        customer = customers[customer_id]
        if amount > customer["balance"]:
            print("Insufficient Balance")
        else:
          customer["balance"] -= amount
          log_transaction(customer, f"Withdrawn {amount}")
          print(f"{amount} Successfully Withdrawn.")
def transfer_money():
    send = input("Enter Sender's ID: ")
    if not send in customers:
        print("Not Found")
        return
    sender = customers[send]
    amount = float(input("Enter Amount To Transfer: "))
    if amount < 0:
        print("Enter Amount Greater Than Zero.")
        if amount > sender["balance"]:
            print("Insufficient Balance")
    else:
        receive = input("Enter Receiver's ID: ").strip().title()
        if not receive in customers:
            print("Not Found")
            return
        receiver = customers[receive]
        if receiver != sender: 
            sender["balance"] -= amount
            receiver["balance"] += amount
        log_transaction(sender, f"Transfered {amount} To {receiver}")
        log_transaction(receiver, f"Received {amount} from {sender}")
        print(f"{amount} Successfully Transfered To {receiver}")
def find_richest_customer():
    richest = max(customers, key= lambda sid: customers[sid]["balance"]) 
    print(f"{customers[richest]["name"]}: {customers[richest]["balance"]}")
def total_bank_balance():
    total = sum(customer["balance"] for customer in customers.values())
    print(total)
def average_balance():
    return {total_bank_balance() / len(customers)}
def delete_customer():
    customer_id = input("Enter Customer ID To Delete: ").strip().title()
    delete = input("Confirm To Delete Customer(yes/no): ")
    if delete == "yes":
        return 
    del customers[customer_id]
    print(f"{customer_id} Deleted Successfully")
    return
def view_transactions():
    customer_id = input("Enter Customer ID: ")
    if customer_id in customers:
        print(f"\nTRANSACTION HISTORY FOR {customers[customer_id]["name"]}:")
        for t in customers[customer_id]["transactions"]:
            if customer_id in customers:
                print(t)
    else:
        print("Customer Not Found.")
while True:
    print("\n==== BANK MANAGEMENT SYSTEM ====\n" \
    "1) Create Customer\n" \
    "2) View All Customers\n" \
    "3) Search Customer\n" \
    "4) Deposit Money\n" \
    "5) Withdraw Money\n" \
    "6) Transfer Money\n" \
    "7) Find Richest Customer\n" \
    "8) Calculate Total Bank Balance\n" \
    "9) Calculate Average Balance\n" \
    "10) Delete Customer\n" \
    "0) Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        create_customer()
    if choice == "2":
        view_all_customers()
    if choice == "3":
        search_customer()
    if choice == "4":
        Deposit_money()
    if choice == "5":
        withdraw_money()
    if choice == "6":
        transfer_money()
    if choice == "7":
        find_richest_customer()
    if choice == "8":
        total_bank_balance()
    if choice == "9":
        average_balance()
    if choice == "10":
        delete_customer()
    if choice == "0":
        log_transaction()
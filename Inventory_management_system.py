inventory = {
    "item1": {
        "name":"Laptop",
        "price": 350000,
        "quantity": 5
    },
    "item2": {
        "name": "Phone",
        "price": 200000,
        "quantity": 10
    },
    "item3": {
        "name": "Headset",
        "price": 25000,
        "quantity": 15
    }
}
def add_item():
    #item_id = input("Enter Item ID")
    name = input("Enter Name Of Item: ")
    if name in inventory:
        print("Name Already Exist")
        return
    price = float(input("Enter Price Of Item: "))
    quantity = int(input("Enter Quantity Of Item: "))
    item_id = f"item{len(inventory)+1}"
    inventory[item_id] = {
        f"name": {name},
        f"price": {price},
        f"quantity": {quantity}
    }
    print(f"{name} Added Successfully.")
def view_items():
    for item in inventory.items():
        print(item)
def search_item():
    search = input("Enter Name Of Item To Search: ").strip().title()
    for item in inventory.values():
        if item["name"] == search:
            print(f"Item Found: {item}")
            return
        print("Not Found.")
def sell_item():
    item_id = input("Enter Item Name To Sell: ")
    #for item_id,details in inventory.items():
    if item_id not in inventory:
        print("Not Found.")
        return
    sell_quantity = int(input("Enter Quantity: "))
    if sell_quantity > inventory[item_id]["quantity"]:
        print("Insufficient Quantity")
        return
    inventory[item_id]["quantity"] -= sell_quantity
    print(f"{sell_quantity} {inventory[item_id]["name"]} Successfully Sold Out for {inventory[item_id]["price"]*sell_quantity}.")
    print(f"{inventory[item_id]["quantity"]} {inventory[item_id]["name"]} Remaining In Stock")
def Restock_item():
    restock = input("Enter ID Of Item To Restock: ").strip().title()
    if restock not in inventory:
        print("Item Not Found.")
        return
    restock_quantity = int(input("Enter Quantity To Restock: "))
    inventory[restock]["quantity"] +=  restock_quantity
    print(f"{restock_quantity} {inventory[restock]["name"]} Restocked Successfully.")
def update_item_price():
    item_id = input("Enter Item ID To Update Price: ").strip()
    #for item_id in inventory.items():
    if item_id in inventory:
        new_price = float(input("Enter New Price: "))
        inventory[item_id]["price"] = new_price
        print(f"{inventory[item_id]["name"]} Price Updated To {new_price}")
        return
    print("Not Found")
def delete_item():
    del_item = input("Enter Item ID To Delete: ")
    if del_item in inventory:
        delete = input("Confirm Delete(yes/no): ")
        if delete != "yes":
            return
        del inventory[del_item]
        print(f"{del_item} Successfully Deleted.")
def total_value():
    #for item_id,details in inventory.items():
    #    each_total = inventory[item_id]["price"] * inventory[item_id]["quantity"]
    each_total = {k: round(v["price"] * v["quantity"],) for k,v in inventory.items()}
    print(each_total)
    inventory_total = sum(each_total.values())
    print(inventory_total)
def most_valuable():
    each_total = {k: round(v["price"] * v["quantity"],) for k,v in inventory.items()}
    highest_value = max(each_total,key=each_total.get)
    print(f"Most Valuable Item: {inventory[highest_value]}")
    print(f"Total Value: {each_total[highest_value]}")
def apply_discount(discount = 20):
    item = input("Enter Item ID To Apply Discount: ").strip()
    if item in inventory:
        old_price = inventory[item]["price"] 
        new_price = inventory[item]["price"] - (old_price * discount / 100)
        inventory[item]["price"] = new_price
        print(f"{discount} Discount Successfully Applied To {item}")

while True:
    print("1.Add Item")
    print("2.View Item")
    print("3.Search Item")
    print("4.sell")
    print("5.Restock")
    print("6.update")
    print("7.delete Item")
    print("8.Calculate Total Inventory Value")
    print("9.Find Most Valuable Item\n" \
          "10.Apply Discount")
    print("0.Exit")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        search_item()
    elif choice == "4":
        sell_item()
    elif choice == "5":
        Restock_item()
    elif choice == "6":
        update_item_price()
    elif choice == "7":
        delete_item()
    elif choice == "8":
        total_value()
    elif choice == "9":
        most_valuable()
    elif choice == "10":
        apply_discount()
    elif choice == "0":
        break
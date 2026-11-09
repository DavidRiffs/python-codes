titles = ["Blue Code","Red Book Of Wisdom","Grow Richer","Heaven On Earth"]
borrowed = []
returned = []
while True:
    print("Welcome To Our Library")
    print("1.Add Book")
    print("2.View Books")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Search Book")
    print("6.Delete Book")
    print("7.Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        added = input("Enter Book Title To Be Added: ").strip().title()
        if added in titles:
            print(f"{added} Already Exists.")
        else:
            titles.append(added)
            print("Book Added Successfully")
    elif choice == "2":
        print("\n List Of Available Books")
        for index, title in enumerate(titles, start=1):
            print(f"{index}: {title}")
    elif choice == "3":
        borrow = input("Enter Book To Borrow: ").strip().title()
        if borrow in titles:
            titles.remove(borrow)
            borrowed.append(borrow)
            print("Book Borrowed Successfully.")
        elif borrow in borrowed:
            print("Book Is Already Borrowed.")
        else:
            print("Book Not Found")
        print(borrowed)
    elif choice == "4":
        returrn = input("Enter Book To Return: ").strip().title()
        if returrn in borrowed:
                borrowed.remove(returrn)
                titles.append(returrn)
                print("Book Successfully Returned.")
        else:
            print("This Book Was Not Borrowed.")
        print("returrn")
    elif choice == "5":
        search = input("Enter Book To Search: ")
        if search in titles:
            print(f"{search} found")
        elif search in borrowed:
            print("Currently Borrowed.")
        else:
            print("Book Not Found")
        if not titles:
            print("No Books In The Library")
        else:
            number_of_books = len(titles)
            print(f"Number Of Books Available: {number_of_books}")
            number_of_borrowed = len(borrowed)
            print(f"Number Of Borrowed Books: {number_of_borrowed}")
    elif choice == "6":
        delete = input("Enter Book To Delete: ").strip().title()
        confirm = input(f"Are You Sure To Delete {delete}(yes/no): ")
        if confirm != "yes":
            continue
        elif delete in titles:
            titles.remove(delete)
            print(f"{delete} Successfully Deleted")
        else:
            print("Book Not Found.")
contacts = {}

while True:
    print("\n1 Add Contact")
    print("2 Show Contacts")
    print("3 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contacts[name] = phone

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        break

    else:
        print("Wrong choice")
        contacts = {}

while True:
    print("\n1 Add Contact")
    print("2 Show Contacts")
    print("3 Search")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        print(contacts)

    elif choice == "3":
        n = input("Enter name to search: ")

        if n in contacts:
            print("Phone:", contacts[n])
        else:
            print("Not found")

    elif choice == "4":
        break

    else:
        print("Wrong choice")
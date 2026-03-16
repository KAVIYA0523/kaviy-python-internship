contacts = {}


# -------- ADD --------
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    contacts[name] = phone
    print("Contact added")


# -------- VIEW --------
def view_contacts():
    if contacts == {}:
        print("No contacts")
    else:
        for name, phone in contacts.items():
            print(name, ":", phone)


# -------- UPDATE --------
def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        phone = input("Enter new phone: ")
        contacts[name] = phone
        print("Updated")
    else:
        print("Not found")


# -------- DELETE --------
def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Deleted")
    else:
        print("Not found")


# -------- SEARCH --------
def search_contact():
    name = input("Enter name to search: ")

    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Not found")


# -------- SAVE TO FILE --------
def save_file():
    file = open("contacts.txt", "w")

    for name, phone in contacts.items():
        file.write(name + "," + phone + "\n")

    file.close()
    print("Saved to file")


# -------- MENU --------
while True:

    print("\n1 Add")
    print("2 View")
    print("3 Update")
    print("4 Delete")
    print("5 Search")
    print("6 Save")
    print("7 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()

    elif choice == "6":
        save_file()

    elif choice == "7":
        break

    else:
        print("Invalid")
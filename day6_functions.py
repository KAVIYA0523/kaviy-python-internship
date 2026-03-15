def add(a, b):
    print("Result:", a + b)

def sub(a, b):
    print("Result:", a - b)

def mul(a, b):
    print("Result:", a * b)

def div(a, b):
    print("Result:", a / b)


while True:
    print("\n1 Add")
    print("2 Sub")
    print("3 Mul")
    print("4 Div")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        break

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    if choice == "1":
        add(a, b)
    elif choice == "2":
        sub(a, b)
    elif choice == "3":
        mul(a, b)
    elif choice == "4":
        div(a, b)
    else:
        print("Wrong choice")
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Wrong input!")
else:
    print("Success! You entered:", num)
finally:
    print("Program finished.")
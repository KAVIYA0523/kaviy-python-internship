numbers = [5, 2, 9, 1, 7]

print("Original:", numbers)

numbers.sort()

print("Sorted:", numbers)

x = int(input("Enter number to search: "))

if x in numbers:
    print("Found")
else:
    print("Not found")
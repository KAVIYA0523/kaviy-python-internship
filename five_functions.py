def square(n):
    print(n*n)

def cube(n):
    print(n*n*n)

def even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

def greet(name):
    print("Hello", name)

def maxnum(a, b):
    if a > b:
        print(a)
    else:
        print(b)


square(4)
cube(3)
even(5)
greet("Kaviya")
maxnum(10, 7)
# 1 reverse string
s = "python"
print(s[::-1])

# 2 count letters
s = "hello"
print(len(s))

# 3 replace
s = "I like java"
print(s.replace("java", "python"))

# 4 check word
s = "python"
print("py" in s)

# 5 split
s = "a,b,c"
print(s.split(","))
# 1 squares
nums = [1,2,3,4]
sq = [x*x for x in nums]
print(sq)

# 2 even numbers
even = [x for x in range(10) if x%2==0]
print(even)

# 3 uppercase
words = ["a","b","c"]
up = [w.upper() for w in words]
print(up)
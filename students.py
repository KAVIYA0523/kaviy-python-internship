import json

# Step 1: Create student data
students = [
    {"name": "Kaviya", "age": 20},
    {"name": "Ravi", "age": 22}
]

# Step 2: SAVE to file (write)
with open("students.json", "w") as file:
    json.dump(students, file)

print("Data saved ✅")

# Step 3: READ from file
with open("students.json", "r") as file:
    data = json.load(file)

print("Data loaded ✅")
print(data)
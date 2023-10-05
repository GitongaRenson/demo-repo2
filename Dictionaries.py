student = {
    "Name": "Mary Masika",
    "Admission": "scm222-0560/2023",
    "Course": "Financial engineering",
    "Home County": "Uasin Gishu",
    "age": 18,
}


print(student)

# using the constructor function to create dictionaries

student2 = dict(nNme="Seline", Course="computer", School="KCA")

print(student2)

print(type(student2))
print(len(student))

# Access items
print(student["Admission"])
print(student.get("age"))

# list all keys
print(student.keys())

# list all values
print(student.values())

# list of key/value pairs as tuples
print(student.items())

# verify a key exists
print("age" in student)


# change values
student["age"] = "16"
student2.update({"age": "18"})

print(student2)
print(student)

# remove items
print(student2.pop("age"))
print(student2)
value = 1
while value < 10:
    print("I'm the G")
value += 1

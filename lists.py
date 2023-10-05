# Working with lists and tuples
users = ["Ann", "James", "Dave"]

data = ["Sara", 42, True]

emptylist = []
# Checking to see if a value is in a list. Should return a boolean value
print("Ann" in users)

# printing a value from a specific position in a list

print(users[0])

# Checking for the last value in our list

print(users[-2])

# Checking the position of a specific value

print(users.index("Ann"))

# Checking for a range of value. Does not include the last value
print(users[0:2])
print(users[1:])

# checking the number of items in a list

print(len(users))

# Adding to list
users.append("Elsa")
print(users)

# Adding two lists
users += ["Dama"]
print(users)

# Extend method
users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)
# picking a specific spot to add to the list
users.insert(1, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

# Replacing users in a list
users[2:3] = ["Bancy", "Peter"]
print(users)

# replacing data in a list
users.remove("Bob")
print(users)

print(users.pop())

# deleting

del users[0]
print(users)

# clearing a list

data.clear()
print(data)

# sorting out data in a list
users.sort()
print(users)

#sorting in alphabetical order
users.sort(key=str.lower)
print(users)
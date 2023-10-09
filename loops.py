# There are two different types of loops. A while loop and a for loop
# A while loop will execute a block of code when a conditin is true

value = 1

# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

# For Loops
# For loops iterate over a sequence i.e collection data types

names = ["Dave", "Sara", "John"]

# for names in names:
#     print(names)


# for x in "mississippi":
#     print(x


# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# for x in range(4):
#   print(x)
# for x in range(2, 203, 5):
#     print(x)
# else:
#     print("Glad thats over")
# Nested loops
actions = ["codes", "eats", "sleeps"]
names = ["Dave", "Sara", "John"]
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")
for action in actions:
    for name in names:
        print(name + " " + action + ".")

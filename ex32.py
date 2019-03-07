theCount = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# For loop goes through a list
for num in theCount:
    print(f"This count is {num}")

for fruit in fruits:
    print(f"This fruit is {fruit}")

for i in change:
    print(f"I got {i}")

# Building a list
elements = []

# Rang(0, 6) == 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to elements")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
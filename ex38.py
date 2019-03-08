tenThings = "Apples Oranges Cows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

stuff = tenThings.split(" ")

moreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    nextOne = moreStuff.pop()
    print("Adding:", nextOne)
    stuff.append(nextOne)
    print("There are", len(stuff), " items right now")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(", ".join(stuff))
print("#".join(stuff[3:6]))
print(stuff)
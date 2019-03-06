people = 20
cats = 30 
dogs = 15

# If statement creates a branch in the code
if people < cats:
    print("Too many cats!")
elif people > cats:
    print("Not too many cats!")

if people < dogs:
    print("The world is drooled on!")
elif people > dogs:
    print("The world is dry")

dogs += 5

if people > dogs:
    print("People > dogs")
elif people < dogs:
    print("people < dogs")
else:
    print("People == dogs")
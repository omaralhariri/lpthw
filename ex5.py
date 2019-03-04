myName = 'Omar Alhariri'
myAge = 25
myHeight = 178
myWeight = 80
myEyes = 'Green'
myTeeth = 'White'
myHair = 'Black'

heightInch = round(myHeight * 0.3937008, 2)
weightPounds = myWeight * 2.205

print(f"Let's talk about {myName}.")
print(f"He's {myHeight} cm tall. Which is {heightInch} in Inches.")
print(f"He's {myWeight} kg heavy. Which is {weightPounds} in Pounds.")
print("That's not too much heavy.")
print(f"He's got {myEyes} eyes and {myHair} hair.")
print(f"He's got {myTeeth} teeth depending on the coffee.")

#this line is tricky
total = myAge + myHeight + myWeight

print(f"If He adds {myAge}, {myHeight},and {myWeight} He gets {total}.")

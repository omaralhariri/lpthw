def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f"You have {cheeseCount} Cheeses!")
    print(f"You have {boxesOfCrackers} boxes of crackers!")

print("Num args:")
cheeseAndCrackers(10, 12)

print("Vars args:")
cheese = 10
boxes = 12

cheeseAndCrackers(cheese, boxes)

print("Math args:")
cheeseAndCrackers(5 + 5, 4 + 8)

print("Vars and math args:")
cheeseAndCrackers(cheese + 2, boxes + 2)
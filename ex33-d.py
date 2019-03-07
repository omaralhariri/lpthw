numbers = []

def addNum(i, maxNum, inc):
    if i < maxNum:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += inc
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")
        addNum(i, maxNum, inc)

addNum(2, 20, 2)

print("The numbers:")
for num in numbers:
    print(num)
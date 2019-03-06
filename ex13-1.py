from sys import argv
script, num1, num2 = argv # Remember to assign vars to argv
# Default type for arguments is string
num1 = int(num1) # Convert them to integers for math operations
num2 = int(num2) # Operation to strings gives a TypeError (unsupported oprand types)

print("Welcome to this simple calculator")

# Defining the function without parameters gives an unboundLocalError
# local variable referenced before assignment
def math(num1, num2):
    print("Your first num is:", num1)
    print("Your second num is:", num2)
    print("Addition is:", num1 + num2)
    print("Subtraction is:", end = ' ')
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)
    print("multiplication is:", num1 * num2)
    print("Division is:", end = " ")
    if (num1 / num2) > 1:
        print(num1 / num2)
    else:
        print(num2 / num1)
    ans = input("Do you want to continue? ")
    ans = str.lower(ans)
    if ans == "y" or ans == "yes":
        num1 = int(input("First number? "))
        num2 = int(input("Second number? "))
        math(num1, num2)
    else:
        print("Bye!")
math(num1, num2)
# Calling the function with the required arquments

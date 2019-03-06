# When passed in function definition, they're called parameters
# When passed as values, they're called arguments
def lots(*args):
    arg1, arg2 = args
    print(f"arg1 = {arg1}, arg2 = {arg2}")

def two(arg1, arg2):
    print(f"agr1 = {arg1}, arg2 = {arg2}")

def one(arg):
    print(f"Here's my lonely argument: {arg}")

def nothing():
    print("Here's nothing!")

lots("Omar", "Alhariri")
two("Anas", "Moh")
one("Alhasan")
nothing()
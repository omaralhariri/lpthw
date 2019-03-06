def add(a, b):
    print(f"Adding: {a}, {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting: {a}, {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying: {a}, {b}")
    return a * b

def divide(a, b):
    print(f"Dividing: {a}, {b}")
    return a / b

age = add(15, 10)
height = subtract(183, 5)
weight = multiply(20, 4)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(what)
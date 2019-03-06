print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs.")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-" * 15)
print(poem)
print("-" * 15)

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 1000
    crates = jars / 100
    return jellyBeans, jars, crates

startPoint = 10000
beans, jars, crates = secretFormula(startPoint)

print("With a starting point of {}".format(startPoint))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

startPoint = startPoint / 10

print("We can also do that this way:")
formula = secretFormula(startPoint)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# .format(*formula))
# Without the * in formula, it will give IndexError: tuple index out of range
# this is an easy way to apply a list to a format string
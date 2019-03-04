typesOfPeople = 10 # assign 10 to the var typesOfPeople
# variable with formatted string to replace the var with its value
x = f"There are {typesOfPeople} types of people:"
binary = "binary"
doNot = "Don't"
y = f"Those who know {binary} and those who {doNot}."

print(x)
print(y)

print(f"I said: {x}") #print a formated string to includer a var value
print(f"I also said: '{y}'") # put the var value inside single quotes

# boolean variable
hilarious = True

#variable with a placeholder for a formated variable
jokeEvaluation = "Isn't that joke funny?! {}"
# using .format() method to replace the placeholder with the variable value
print(jokeEvaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# concatination of string
print(w + e)

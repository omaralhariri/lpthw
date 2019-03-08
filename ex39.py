# Create a mapping of states to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# Creat a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# Adding some moe cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# Print out some cities
print("-" * 10)
print("NY state has:", cities["NY"])
print("OR state has:", cities["OR"])

# Print out some states
print("-" * 10)
print("Michigan's abbreviation is:", states["Michigan"])
print("Florida's abbreviation is:", states["Florida"])

# Do it by using the state then cities dict
print("-" * 10)
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

# Print every state abbreviation
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} abbrev is {abbrev}")

# Print every city in state
print("-" * 10)
for state, city in list(cities.items()):
    print(f"{state} has {city}")

# Do both at the same time
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"And has city {cities[abbrev]}")

print("-" * 10)
# Safely get an abbreviation for a state thet might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# Get a city with a defaul value
city = cities.get("TX", "Does not exist")
print(f"The city for the state TX is: {city}")

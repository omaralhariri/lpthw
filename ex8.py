# template string
formatter = "{} {} {} {}"
# adding numbers to each placeholder in the template
print(formatter.format(1, 2, 3, 4))
#adding a string to each placeholder in the string template
print(formatter.format("One", "Two", "Three", "Four"))
# Adding a boolean value to each placeholder in the template
print(formatter.format(True, False, False, True))
# Repeating the template in each place holder in the template
print(formatter.format(formatter, formatter, formatter, formatter))
# Adding a string to each placeholder in the template, they will be on one line
print(formatter.format(
    "I could do it",
    "With some passion, honey",
    "I could do it",
    "I could love YOU!"
))

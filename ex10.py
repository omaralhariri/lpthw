tabbyCat = "\tI'm tabbed in." # insert a tab-space before text
persianCat = "I'm split\non a line." # the next will be on a new line
backslashCat = "I'm \\ a \\ cat." #escaping \, will print one \
oneQuote = 'I\'m good'  # escape single quote inside single quoted string
# \n\t will add new line then add tap--space
fatCat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabbyCat)
print(persianCat)
print(backslashCat)
print(fatCat)
print(oneQuote)

bell = "using slash a\aso" # i don't know what it does
print(bell)

backspace = " what slash b \bdoes" # remove previous character
print(backspace)

formfeed = " what slash f \fdoes" # adds a new line and spaces till it reaches
# the position of it in the previous line
#what slash f
#             does
print(formfeed)

#named = " what slash N{name} \N{name} does"
#for unicode only
#print(named)

carriageReturn = "what it \r does"
print(carriageReturn)

# return to page 62 in lpthw

print('''
am i really going to use
three single quotes
instead of double quotes
maybe, it's easier to write
''')

print(f"{bell} and {tabbyCat} and {persianCat} all with  {backspace}")

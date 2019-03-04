print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # will rpeat string 10 times (..........)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"


print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ') # the below comment
print(end7 + end8 + end9 + end10 + end11 + end12)

# Removing the comma (,), throw a SyntaxError. [end6 end = ' ']
#replacing it with a + sign throw a SyntaxError (keyword can't be an exxpression)
# [end6 + end = ' ']
#putting the expression in parenthesies [ end6 + (end = ' ')]
# throw a SyntacsError (invalid syntax)

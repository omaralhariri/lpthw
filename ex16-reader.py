# from sys import argv
# script, filename = argv
filename = input("Which file you wanna see? ")
filename += ".txt"
print("Here's your file:")
txt = open(filename)
print(txt.read())
txt.close()
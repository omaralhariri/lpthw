from sys import argv
script, inputFile = argv

def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printLine(lineCount, f):
    print(lineCount, f.readline())

currentFile = open(inputFile)

print("First, let's print the whole file:\n")

printAll(currentFile)

print("Now, let's rewind.")
rewind(currentFile)

print("Now, let's print three lines:\n")

currentLine = 1
printLine(currentLine, currentFile)

currentLine += 1
printLine(currentLine, currentFile)

currentLine += 1
printLine(currentLine, currentFile)
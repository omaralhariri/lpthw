filename = input("What file do you wanna open? ")
filename += ".txt"

def readAll(f):
    openF = open(f).read()
    return openF

def readLine(startLine, f):
    openF = open(f)
    openF.seek(startLine)
    readF = openF.read()
    openF.close()
    return readF

reading = input("Do you want to see all of its content? ")
reading = str.lower(reading)
if reading[0] == "y":
    print(readAll(filename))
else:
    lines = int(input("How many lines do want to see?"))
    if lines == 0:
        print ("See ya later!")
    elif lines < 0:
        print ("Must insert a positive number!")
    else:
        startLine = int(input("Where do you wanna start reading the file?"))
        print(readLine(startLine, filename))
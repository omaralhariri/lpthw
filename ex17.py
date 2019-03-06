from sys import argv
from os.path import exists

script, fromFile, toFile = argv

# This is a string and not a file to be closed
inFile = open(fromFile).read()

print(f"The input file is {len(inFile)} bytes long")

# If it doesn't exist, it will create it
# If it exist, it will truncate it and copy the data from first file
print(f"Does the output file exists? {exists(toFile)}")

outFile = open(toFile, 'w')
outFile.write(inFile)

print("All Done!")

#Can't use the close attribute because it's a string not a file object
# inFile.close()

# Just Close it and avoid memory lack, locking, losing data 
outFile.close()
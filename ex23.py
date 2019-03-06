import sys
script, encoding, error = sys.argv

#Recursive function until the end of the file
def main(langFile, encoding, errors):
    
    # Read the first line, then move the cursor to the next line
    line = langFile.readline()

    # If line does exist, call outLine() and call main() itself too
    # If the next line is empty, then leave the function, don't call it
    if line:
        outLine(line, encoding, errors)
        return main(langFile, encoding, errors)

def outLine(line, encoding, errors):
    # Strip the string from chars at its beginning and end of line, like(\n)
    nextLang = line.strip()
    # Encodes the string into bytes
    rawBytes = nextLang.encode(encoding, errors=errors)
    # Decode bytes into string
    cookedString = rawBytes.decode(encoding, errors=errors)

    print(rawBytes, "<====>", cookedString)

# Openning the file with the desired decoding
langs = open("languages.txt", encoding="utf-8")

main(langs, encoding, error)
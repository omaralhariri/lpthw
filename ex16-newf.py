question = input("Wanna create a new file? (Yes or No) ")
question = str.lower(question) 
if question[0] == "y":
    filename = input("Write the name of the file...\n")
    filename = filename + ".txt" # Just to turn it a text file
    newFile = open(filename, 'x') # Create a new file and open for writing
    fileContent = input(f""" Write {filename}'s content...\n""")
    newFile.write(fileContent)
    print("Done! Good job!")

    reviewQ = input("Wanna review the file's content? (Y or N) ")
    reviewQ = str.lower(reviewQ)
    if reviewQ[0] == "y":
        print(f"Here's your {filename} content:")
        newFile = open(filename) # Open the file in reading mode to be readable
        print(newFile.read())
    else:
        print("See ya later!")
    
    newFile.close()
else:
    print("Come back when you have the idea!")
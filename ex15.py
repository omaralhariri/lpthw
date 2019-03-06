# from sys import argv
# script, filename = argv

# # Open the file in the argv 
# txt = open(filename)
# print(f"Here's your {filename}:")
# # Read the file assigned to var txt using read() meathod
# print(txt.read())
# txt.close()

# Getting the file from users is better, because it gives them the choice 

print("\nType the filename you want to open:")
fileAgain = input(">> ")

txtAgain = open(fileAgain)

print("Here it is:\n")
print(txtAgain.read())
txtAgain.close()



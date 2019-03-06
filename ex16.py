from sys import argv
script, filename = argv
print(f"We're going to earase {filename}.")
print(f"If you don't want that, hit CTRL+c (^C).")
print(f"If you do want that, hit ENTER.")

input("?")

print("Openning the file...")

# Opening the file in read mode 'r', the default, to show it's content before
# deleting it.
# target = open(filename)
# print(target.read())

# Opening a file in write mode 'w', will delete it's content
# 'a' append, keeps the content of the file and move the cursor to on the end
# of the file with no new line. Mode 'a' is unreadable, same as mode 'w'
# 'a+' is readable, but reads the first line only, which will always be empty
# when using 'a'
# mode 'w+' is does the same for the file, empties it, but it's readable!
target = open(filename, 'w') 

# Using 'w' doesn't need the use of truncate
# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for 3 lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

# write(text), takes exactly one parameter 
target.write(f"""{line1}\n{line2}\n{line3}""")

print("Finally, we close it")
target.close()  
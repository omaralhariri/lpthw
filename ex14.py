from sys import argv
script, username = argv
promot = ">> "

print(f"Hi {username}, I'm the {script} script")
print(f"Do you like me {username}?")
likes = input(promot)

print(f"Where do you live?")
lives = input(promot)

print("What kind of computer do you have?")
computer = input(promot)

print(f'''
So, you said {likes} about liking me.
and you live in {lives}
and you have a {computer} computer.
''')
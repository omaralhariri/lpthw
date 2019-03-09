from other import Other
# ([from . import other] or [import other]):
# Gives an error (Other() is not defined)
# Importing your module:
# from module import class
# Module: the module your class is in
# Class: the class you want to use inside that module

# class Other(object):
    
#     def implicit(self):
#         print("OTHER implicit()")

#     def override(self):
#         print("OTHER override()")

#     def altered(self):
#         print("OTHER altered()")

class Child(object):
    
    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD overrid()")

    def altered(self):
        print("CHILD, BEFORE...")
        self.other.altered()
        print("CHILD, AFTER...")

other = Other()
son = Child()

other.implicit()
son.implicit()

other.override()
son.override()

other.altered()
son.altered()
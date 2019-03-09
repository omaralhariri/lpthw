class Parent(object):  # Make a class Parent is-a object (type)

    def implicit(self):  # Define the Parent version of the method implicit
        print("PARENT implicit()")  # Message to print when the method is called

    def override(self):  # Parent version of override
        print("PARENT override()")  # Message to print

    def altered(self):  # Parent version of altered
        print("PARENT altered()")  # Message to print

class Child(Parent):  # Make a class Child is-a Parent (type)
    
    def override(self):  # Child version of override
        print("CHILD override()")  

    def altered(self):  # Child version of altered
        print("CHILD, BEFORE PARENT altered()")  # Printed out when altered called
        # Calls super() function with Child (class) & self arguments
        # The function returns the parent of the Child class which is Parent
        # Then calling the parent version of the altered() method
        # Exceution statement: Parent.altered('self')
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()  # Set dad as an instance of Parent()
son = Child()   # Set son as an instance of Child() -> inherit Parent()

dad.implicit()  # Calling implicit method on the dad instance -> PARENT implicit()
son.implicit()  # Calling implicit method on the son instance -> PARENT implicit()
                # Same output as dad because it Inherit it from the parent class

dad.override()  # PARENT overrid()
son.override()  # CHILD override() -> because it's "redifined" in the child class

dad.altered()  # PARENT altered()
son.altered()  # CHILD, BEFORE ...
               # PARENT altered()
               # CHILD, AFTER ...
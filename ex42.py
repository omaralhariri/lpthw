## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a __init__ that takes self and name params
        self.name = name

## Class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a __init__ that takes self and name params
        self.name = name

## Class Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## Class Person has-a __init__ that takes self and name params
        self.name = name

        ## Person has-a pet attribute 
        self.pet = None

## Class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Class Employee has-a __init__ that takes self, name, and salary params
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Class Fish is-a object
class Fish(object):
    pass

# Class Salmon is-a Fish
class Salmon(Fish):
    pass

## Class Halibut is-a Fish
class Halibut(Fish):
    pass

## Rover is-a Dog (instance of Dog with a name Rover)
rover = Dog("Rover")

## Satan is-a Cat with name "Satan"
satan = Cat("Satan")

## Mary is-a Person with name Mary
mary = Person("Mary")

## Mary has-a pet attribut which is satan
mary.pet = satan

## Frank is-a Employee with name Frank and salary = 120000
frank = Employee("Frank", 120000)

## Frank has-a pet attribute 
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## Crouse is-a Salmon
course = Salmon()

## Harry is-a Halibut
harry = Halibut()
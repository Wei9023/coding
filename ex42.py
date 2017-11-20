## Animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Class Dog has-a __init__ that takes self and name parameters
class Dog(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to name
        self.name = name

## Class Cat has-a __init__ that takes self and name parameters
class Cat(Animal):

    def __init__(self, name):
        ## From self get the name attribute and set it to name
        self.name = name

## Class Person has-a __init__ that takes self and name parameters
class Person(object):

    def __init__(self, name):
        ##From self get the name attribute and set it to name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class Employee has-a __init__ that takes self, name and salary parameters
class Emplyee(Person):

    def __init__(self, name, salary):
        ## From super get the __init__ function, and call it with parameters name
        super(Employee, self).__init__(name)
        ## From self get the salary attribute and set it to salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to Satan
mary.pet = Satan

##
frank = Employee("Frank", 120000)

## From frank get the pet attribute and set it to rover
frank.pet = rover

## set flipper to a instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()

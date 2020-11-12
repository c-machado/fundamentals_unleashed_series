class Dog():

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    #self to connect with the object, so the dog 'Lola' can bark :)
    def bark(self, number):
        print("Woof, my name is {} and the number is {}" .format(self.name, number))


myDog = Dog('Criollo', 'Lola')
myDog.bark(3)

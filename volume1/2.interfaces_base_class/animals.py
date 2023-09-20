from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name, age, gender) -> None:
        super().__init__()
        self.name=name
        self.age=age
        self.gender=gender

    @abstractmethod
    def produce_sound():
        pass

    def __str__(self):
        return f" name: {self.name} age: {self.age} and gender: {self.gender}"

class Dog(Animal):
    #  def __init__(self, name, age, gender) -> None:
    #      super().__init__(name, age, gender)

     def produce_sound(self):
        return 'bark'

class Frog(Animal):
    # def __init__(self, name, age, gender) -> None:
    #     super().__init__(name, age, gender)

    def produce_sound():
        print('crock')

class Cat(Animal):
    # def __init__(self, name, age, gender) -> None:
    #     super().__init__(name, age, gender)

    def produce_sound(self):
        return 'meow'

class Kitten(Cat):
    def __init__(self, age) -> None:
        super().__init__ ("kitten", "Female", age)
    

class Tomcat(Cat):
    def __init__(self, age) -> None:
        super().__init__("Tomcat", age, "Male")
    
if __name__ == "__main__":
    dog = Dog('lola',13,'female')
    print(f"Kind of animal{dog}\nAnd produces this sound: '{dog.produce_sound()}'")
    cat = Cat('luna',5,'female')
    print(f"Kind of animal{cat}\nAnd produces this sound: '{cat.produce_sound()}'")
    kitten = Kitten(5)
    print(f"Kind of animal{kitten}\nAnd produces this sound: '{kitten.produce_sound()}'")

# Create a hierarchy of Animals. Your task is simple: there should be a base class which all others derive from. 
# Your program should have 3 different animals dog, Frog and Cat. Create deeper hierarchy and add two additional 
# classes Kitten which is Female and Tomcat which is male. Along with the animals there should be also a class which 
# classifies its derived classes as sound producible. You may guss that all animals are sound producible. 
# The only mandatory functionality of all sound producible objects is to ProduceSound(). 
# For instance the dog should bark. Your task is to model the hierarchy  and test its functionality . 
# Create an animal of each kind and make them produce sound. on the console, for each animal you've instantiated, 
# print its info in three lines: on the first line, print:{kind of animal}, on the second line print: {name} {gender} {age} 
# on the third print the sound it produces {produceSound()} each animal should have name, gender and age, if you enter
#  invalid input for one of the properties throw an exception: 'invalid input;


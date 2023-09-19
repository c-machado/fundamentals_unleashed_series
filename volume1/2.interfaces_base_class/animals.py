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


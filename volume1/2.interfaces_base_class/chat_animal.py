class SoundProducible:
    def produce_sound(self):
        pass


class Animal(SoundProducible):
    def __init__(self, kind, name, gender, age):
        if not all(isinstance(prop, str) for prop in [kind, name, gender]) or not isinstance(age, int):
            raise ValueError("Invalid input")
        self.kind = kind
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.kind}\n{self.name} {self.gender} {self.age}\n{self.produce_sound()}"


class Dog(Animal):
    def produce_sound(self):
        return "Bark"


class Frog(Animal):
    def produce_sound(self):
        return "Ribbit"


class Cat(Animal):
    def produce_sound(self):
        return "Meow"


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__("Kitten", name, "Female", age)


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__("Tomcat", name, "Male", age)


# Example usage:
try:
    dog = Dog("Dog", "Buddy", "Male", 3)
    print(dog)

    frog = Frog("Frog", "Kermit", "Male", 5)
    print(frog)

    cat = Cat("Cat", "Whiskers", "Female", 2)
    print(cat)

    kitten = Kitten("Kitty", 1)
    print(kitten)

    tomcat = Tomcat("Tommy", 4)
    print(tomcat)

    # Uncomment the line below to see the exception message for invalid input.
    # invalid_animal = Dog("Dog", "Rover", 3, "Male")

except ValueError as e:
    print(f"Error: {e}")
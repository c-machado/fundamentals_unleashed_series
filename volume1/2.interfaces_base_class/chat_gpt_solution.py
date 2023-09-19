class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age} years old)"

    def compare_age(self, other_person):
        if self.age < other_person.age:
            return f"{self.name} is younger than {other_person.name}."
        elif self.age > other_person.age:
            return f"{self.name} is older than {other_person.name}."
        else:
            return f"{self.name} and {other_person.name} are the same age."


class Child(Person):
    def __init__(self, name, age, parent_name):
        super().__init__(name, age)
        self.parent_name = parent_name

    def __str__(self):
        return f"{self.name} ({self.age} years old, child of {self.parent_name})"


# Creating two Person instances
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Comparing the ages of two people
age_comparison = person1.compare_age(person2)
print(age_comparison)

# Creating two Child instances
child1 = Child("Eva", 8, "Alice")
child2 = Child("David", 6, "Bob")

# Comparing the ages of two children
child_age_comparison = child1.compare_age(child2)
print(child_age_comparison)
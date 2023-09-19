class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"{self.name} ({self.age} years old, {'Adult' if self.is_adult() else 'Child'})"

    def __eq__(self, other):
        if isinstance(other, Person):
            return id(self) == id(other)
        return False


class Child(Person):
    def __init__(self, name, age, parent_name):
        if age > 15:
            raise ValueError("Child's age cannot be more than 15.")
        super().__init__(name, age)
        self.parent_name = parent_name

    def __str__(self):
        return f"{self.name} ({self.age} years old, Child of {self.parent_name})"


# Example usage:
if __name__ == "__main__":
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 35)
    child1 = Child("Charlie", 8, "Alice")
    child2 = Child("David", 6, "Bob")

    # Compare whether two people are the same by comparing their IDs
    are_people_same = person1 == person1
    print(f"Are person1 and person2 the same? {are_people_same}")

    are_children_same = child1 == child2
    print(f"Are child1 and child2 the same? {are_children_same}")
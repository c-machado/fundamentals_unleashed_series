from abc import ABC, ABCMeta, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def age(self, person_age):
        pass

    @abstractmethod
    def name(self, person_name):
        pass

class Child(Person):
    def __init__(self, name, age):
        super.__init__(name, age)

    def age(self, age):
        if age>15 or age<0:
            raise ValueError(f' enter a valid age, valid range from 1 to 15')
        else:
            print(f' the age of the child is {age}')
    def name(self, person_name):
        pass

# class Adult(Person):
#     def age(self,adult_age):
#         if  adult_age<0:
#             print('enter a valid age, greater than 0')
#         else:
#             print(f' the age of the adult is {adult_age}')


if __name__ == '__main__':
    child = Child('carolina', 37)
    child.age(10)
    # Child().age(13)
    # Adult().age(35)
    # person2 = People('gabriel', 10)
# You can iterate through the keys of a dictionary using a for loop. By default, iterating through a dictionary iterates over its keys.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in my_dict:
    print(key, my_dict[key])


# You can use the items() method to iterate through both keys and values as pairs. This method returns a tuple of key-value pairs that you can unpack in the loop.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key, value in my_dict.items():
    print(key, value)


# Iterating Through Values:
# If you only need to iterate through the values, you can use the values() method.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for value in my_dict.values():
    print(value)


# You can also create a new dictionary or perform some operation while iterating through a dictionary using a dictionary comprehension.

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

new_dict = {key: value for key, value in my_dict.items()}
print(new_dict)


# If you want to iterate through the keys in a specific order (e.g., sorted order), you can use the sorted() function.

my_dict = {'b': 2, 'a': 1, 'c': 3}

for key in sorted(my_dict):
    print(key, my_dict[key])


# To add values to a dictionary in Python, you can use one of the following methods:

# Using the Square Bracket Notation:
# You can add a new key-value pair to a dictionary by using the square bracket notation. If the key already exists, 
# it will update the existing value; otherwise, it will create a new key-value pair.

my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'Alice'
my_dict['age'] = 30
my_dict['city'] = 'New York'

print(my_dict)


# The update() method allows you to add multiple key-value pairs to a dictionary at once.

my_dict = {}

# Adding key-value pairs using update()
my_dict.update({'name': 'Alice', 'age': 30, 'city': 'New York'})

print(my_dict)
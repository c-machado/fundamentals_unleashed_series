# Anonymous Functions: Lambdas allow you to define small, unnamed functions on the fly, without having to give them a specific name. 
# This is useful when you need a simple function for a short duration and don't want to define a separate named function.

# Using a lambda to define an anonymous function
square = lambda x: x ** 2
result = square(5)  # result is 25



# Passing Functions as Arguments: Lambdas can be used to pass functions as arguments to other functions. 
# This is common in functional programming and is useful for operations like sorting, filtering, and mapping.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Sorting using a lambda function as the key
sorted_numbers = sorted(numbers, key=lambda x: -x)


# Short-lived Functions: Lambdas are handy when you need a small function
#  for a specific purpose and don't want to clutter your code with unnecessary function definitions. They are often used for one-off operations.
# Using a lambda to filter a list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))


# Functional Programming: Lambdas are commonly used in functional programming paradigms where functions are treated as first-class citizens. 
# This means functions can be assigned to variables, passed as arguments, and returned as values.



# Concise Code: Lambdas can make code more concise and readable for simple operations, 
# especially when combined with higher-order functions like map, filter, and reduce.
# Using lambda with map
squared_numbers = list(map(lambda x: x ** 2, numbers))

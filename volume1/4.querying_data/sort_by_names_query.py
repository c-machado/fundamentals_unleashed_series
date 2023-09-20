
# Using pandas with Query and lambda expressions, sort the workers by first and last names in descending order

import pandas as pd

workers = [
    {"FirstName": "John", "LastName": "Doe", "Age":20},
    {"FirstName": "Jane", "LastName": "Smith", "Age":30},
    {"FirstName": "Bob", "LastName": "Johnson", "Age":10},
    {"FirstName": "Alice", "LastName": "Brown", "Age":40},
    {"FirstName": "Eva", "LastName": "Davis", "Age":50}
]

data = pd.DataFrame(workers)

age = data.query('Age>20')
# sorted_names = data.query("FirstName == Alice")

print(age)


# List Comprehensions: Python's list comprehensions provide a concise way to create lists based on existing lists. 
# They are often used for filtering and projecting data.
workers = [
    {"FirstName": "John", "LastName": "Doe", "Age": 22},
    {"FirstName": "Jane", "LastName": "Smith", "Age": 19},
    {"FirstName": "Carolina", "LastName": "Machado", "Age": 37},
    # ... other worker dictionaries ...
]

young_workers = [
    {"FirstName": worker["FirstName"], "LastName": worker["LastName"]}
    for worker in workers
    if 18 <= worker["Age"] <= 24
]

print(young_workers)



# Filter and Map Functions: Python provides built-in filter() and map() functions that can be used to filter and project data.

workers = [
    {"FirstName": "John", "LastName": "Doe", "Age": 22},
    {"FirstName": "Jane", "LastName": "Smith", "Age": 19},
    {"FirstName": "Carolina", "LastName": "Machado", "Age": 37},
    # ... other worker dictionaries ...
]

young_workers = list(
    # The map function is a convenient way to apply a function to all elements of an iterable without having to write explicit loops, 
    # making your code more concise and readable.
    map(lambda worker: {"FirstName": worker["FirstName"], "LastName": worker["LastName"]},
        filter(lambda worker: 18 <= worker["Age"] <= 24, workers))
)

print(young_workers)


# Pandas: If you are working with data frames, Pandas is a powerful library for data manipulation that provides similar querying and 
# transformation capabilities to LINQ. It is widely used for data analysis and manipulation.

import pandas as pd

data = pd.DataFrame(workers)

young_workers = data[(data["Age"] >= 18) & (data["Age"] <= 24)][["FirstName", "LastName"]]

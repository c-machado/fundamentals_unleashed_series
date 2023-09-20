# Using the extension methods map, sorted / pandas with lambda expressions, sort the workers by first and last names in descending order

import pandas as pd

workers = [
    {"FirstName": "John", "LastName": "Doe", "Age":"20"},
    {"FirstName": "Jane", "LastName": "Smith", "Age":"30"},
    {"FirstName": "Bob", "LastName": "Johnson", "Age":"10"},
    {"FirstName": "Alice", "LastName": "Brown", "Age":"40"},
    {"FirstName": "Eva", "LastName": "Davis", "Age":"50"}
]

data = pd.DataFrame(workers)
# sorted the names descendenly
# sorted_names_workers = data.sort_values("FirstName", ascending=False)

sorted_names_workers = data.sort_values(by=["FirstName", "LastName"], ascending=[False, False], key=lambda x:x.str.lower())

print(sorted_names_workers)

# worker is an iterable with the first and last names
sorted_names = map(lambda worker: {"FirstName": worker["FirstName"], "LastName": worker["LastName"]},
    # sorted the workers list descendenly base on the first name
    sorted(workers, key = lambda worker:(worker["FirstName"], worker["LastName"]), reverse=True))
    # sorted(workers, key = lambda worker:worker["FirstName"], reverse=True))

# print(list(sorted_names))


workers = [
    {"FirstName": "John", "LastName": "Doe", "Age":"20"},
    {"FirstName": "Jane", "LastName": "Smith", "Age":"30"},
    {"FirstName": "Bob", "LastName": "Johnson", "Age":"10"},
    {"FirstName": "Alice", "LastName": "Brown", "Age":"40"},
    {"FirstName": "Eva", "LastName": "Davis", "Age":"50"}
]

# Use the sorted function with a lambda key function to sort by last name, then first name in descending order
sorted_workers = sorted(workers, key=lambda worker: (worker["LastName"], worker["FirstName"]), reverse=True)

# Print the sorted workers
# for worker in sorted_workers:
    # print(worker)


import pandas as pd

data = {
    "FirstName": ["John", "Jane", "Bob", "Alice", "Eva"],
    "LastName": ["Doe", "Smith", "Johnson", "Brown", "Davis"]
}

df = pd.DataFrame(data)

# Use the sort_values method with lambda expressions to sort by last name, then first name in descending order
sorted_df = df.sort_values(by=["LastName", "FirstName"], ascending=[False, False], key=lambda x: x.str.lower())

# Print the sorted DataFrame
# print(sorted_df)

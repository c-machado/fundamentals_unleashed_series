# write a linq query using the method sintax that finds the first name and last name of all workers between 18 and 24

import pandas as pd

workers = [
    {"FirstName": "John", "LastName": "Doe", "Age": 22},
    {"FirstName": "Jane", "LastName": "Smith", "Age": 19},
    {"FirstName": "Carolina", "LastName": "Machado", "Age": 37},
    {"FirstName": "Gabriel", "LastName": "Martinez", "Age": 10},
]

data = pd.DataFrame(workers)

young_workers = data[(data["Age"] >= 18) & (data["Age"] <= 24)][["FirstName", "LastName", "Age"]]

print(young_workers)

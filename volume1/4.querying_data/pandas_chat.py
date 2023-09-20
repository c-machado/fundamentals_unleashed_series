import pandas as pd

workers = [
    {"FirstName": "John", "LastName": "Doe", "Age": "20"},
    {"FirstName": "Jane", "LastName": "Smith", "Age": "30"},
    {"FirstName": "Bob", "LastName": "Johnson", "Age": "10"},
    {"FirstName": "Alice", "LastName": "Brown", "Age": "40"},
    {"FirstName": "Eva", "LastName": "Davis", "Age": "50"}
]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(workers)

# Use the sort_values method with lambda expressions to sort by last name, then first name in descending order
# sorted_df = df.sort_values(by=["LastName", "FirstName"], ascending=[False, False], key=lambda x: x.str.lower())
sorted_df = df.sort_values(by=["LastName","FirstName"], ascending=[False, False], key=lambda x:x.str.lower())


# Print the sorted DataFrame
print(sorted_df)

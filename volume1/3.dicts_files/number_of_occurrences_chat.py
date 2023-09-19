def count_occurrences(arr):
    # Create an empty dictionary to store the counts
    count_dict = {}

    # Iterate through the array
    for value in arr:
        # Check if the value is already in the dictionary
        if value in count_dict:
            # If it is, increment the count
            count_dict[value] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            count_dict[value] = 1

    return count_dict

# Example usage:
if __name__ == "__main__":
    # Input array of double values
    double_values = [1.2, 2.3, 1.2, 3.4, 2.3, 1.2, 4.5, 3.4]

    # Call the function to count occurrences
    result = count_occurrences(double_values)

    # Print the counts
    for key, value in result.items():
        print(f"{key}: {value} times")
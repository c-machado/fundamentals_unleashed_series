from collections import Counter

# Write a program that reads a list of words from a file words.txt and finds how many times each word is contained in another
# file test.txt. The result should be written in the file result.txt, and the number of their ocurrences should sort in descending
# order. Handle all possible exceptions in your methods

def read_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {str(e)}")

def count_word_occurrences(words, text):
    # Count word occurrences in the text
    # The Counter class in Python is part of the collections module and is used for counting the occurrences of
    #  elements in a collection, such as a list, tuple, string, or other iterable. It's particularly useful
    #  when you need to determine the frequency of items in a collection
    word_count = Counter(text.split())
    
    # Initialize a dictionary to store the results
    results = {}
    
    # Count how many times each word from the list appears in the text
    for word in words:
        # counter.get(element, default_value)
        results[word] = word_count.get(word, 0)
    
    return results

def write_results_to_file(results, output_file_path):
    try:
        with open(output_file_path, "w") as output_file:
            # Sort results by count in descending order
            sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
            
            for word, count in sorted_results:
                output_file.write(f"{word}: {count}\n")
        
        print(f"Results written to '{output_file_path}'.")

    except Exception as e:
        raise Exception(f"An error occurred while writing results to the file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    words_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/words.txt"    # Replace with the path to your words list file
    text_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test.txt"      # Replace with the path to your text file
    output_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/result.txt"  # Replace with the desired output file path

    try:
        # Read words from words.txt
        words = read_words_from_file(words_file_path)

        # Read text from test.txt
        with open(text_file_path, "r") as text_file:
            text = text_file.read()

        # Count word occurrences
        results = count_word_occurrences(words, text)

        # Write results to result.txt
        write_results_to_file(results, output_file_path)
    except Exception as e:
        print(f"Error: {str(e)}")
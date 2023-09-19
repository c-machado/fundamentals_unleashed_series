class RemoveRepeatedWordsTwoFiles:
# write a program that removes from a text file all words listed in another text file. 
# Handle exceptions in your methods

    def remove_repeated_words_from_two_files(input_file_1, input_file_2, output_file):

        try:
            with open(input_file_1, "r") as infile_1:
                lines_infile_1 = infile_1.readlines()
            with open(input_file_2, "r") as infile_2:
                lines_infile_2 = infile_2.readlines()

            words_file_1 = []
            words_file_2 = []
            words_file_3 = []


            for line_1, line_2 in zip(lines_infile_1, lines_infile_2):
                words_file_1 = line_1.split(' ')
                print(f'words_file_1 {words_file_1}')
                words_file_2 = line_2.split(' ')
                print(f'words_file_2 {words_file_2}')
                for word1, word2 in zip(words_file_1, words_file_2):
                    if word1 != word2:
                        words_file_3.append(word1+" ")
            with open(output_file, "w") as outfile:
                outfile.writelines(words_file_3)

            print(f"Filtered content saved to '{output_file}'.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def read_words_to_remove(file_path):
        try:
            with open(file_path, "r") as file:
                words = file.read().split()
            return words
        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {str(e)}")

    def remove_words_from_file(input_file_path, words_to_remove, output_file_path):
        try:
            with open(input_file_path, "r") as input_file:
                lines = input_file.readlines()

            # Create a set of words to remove for faster lookup
            words_to_remove_set = set(words_to_remove)

            filtered_lines = []

            for line in lines:
                # Split the line into words
                words = line.split()

                # Filter out words that are not in the words to remove set
                filtered_words = [word for word in words if word not in words_to_remove_set]

                # Join the filtered words back into a line
                filtered_line = " ".join(filtered_words)
                filtered_lines.append(filtered_line)

            with open(output_file_path, "w") as output_file:
                output_file.writelines(filtered_lines)

            print(f"Words removed and content saved to '{output_file_path}'.")

        except FileNotFoundError:
            raise Exception(f"File not found: {input_file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while processing the file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    words_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/words_1.txt"  # Replace with the path to your words list file
    input_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/words_2.txt"            # Replace with the path to your input text file
    output_file_path = "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/words_not_repeated.txt"          # Replace with the desired output file path

    try:
        words_to_remove = RemoveRepeatedWordsTwoFiles.read_words_to_remove(words_file_path)
        RemoveRepeatedWordsTwoFiles.remove_words_from_file(input_file_path, words_to_remove, output_file_path)
    except Exception as e:
        print(f"Error: {str(e)}")


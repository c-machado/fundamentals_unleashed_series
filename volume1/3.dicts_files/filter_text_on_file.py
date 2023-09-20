# write a program that deltes from a text file all words that start with the prefix "test". 
# The words should contain only the symbols 0...9, a...z, A...Z, _

import re
class deleteLinesContainsText:

    def delete_line_contains_test():
        try:
            with open("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_prefix.txt", 'w+') as file1:
                regex = re.compile('[@!#$%^&*()<>?/\|}{~:]')
                regex1= re.compile('[a-zA-Z0-9]')
                lines = file1.readlines()
                # file1.seek(0)
                x =  [file1.write(line) for line in enumerate(lines) if re.search(regex1, line[0]) and not re.search(regex,line[0]) and re.search("^test", line[0]) ]
        except FileNotFoundError:
            print(f'file not found')
        except Exception as e:
            print(f'un error has occured {str(e)}')

    def filter_words(input_file, output_file):
        try:
            with open(input_file, "r") as infile:
                lines = infile.readlines()
                infile.seek(0)
                filtered_lines = []
                for line in lines:
                    if not line.startswith("test") and re.match("^[0-9a-zA-Z_]+$", line):
                            print(f'line: {line}')
                            filtered_lines.append(line)
 
            with open(output_file, "w") as outfile:
                outfile.writelines(filtered_lines)

            print(f"Filtered content saved to '{output_file}'.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def filter_words_chat(input_file, output_file):
        try:
            with open(input_file, "r") as infile:
                lines = infile.readlines()

            filtered_lines = []

            for line in lines:
                words = line.split()
                filtered_words = []

                for word in words:
                    # Check if the word starts with "test" and contains only allowed symbols
                    if not word.startswith("test") and re.match("^[0-9a-zA-Z_]+$", word):
                        filtered_words.append(word)

                filtered_line = " ".join(filtered_words)
                filtered_lines.append(filtered_line)

            with open(output_file, "w") as outfile:
                outfile.writelines(filtered_lines)

            print(f"Filtered content saved to '{output_file}'.")

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == "__main__":

  
    deleteLinesContainsText.delete_line_contains_test()
    deleteLinesContainsText.filter_words("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_prefix.txt",
                                     "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_prefix_filtered.txt")
    deleteLinesContainsText.filter_words_chat("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_prefix.txt",
    "/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test_prefix_filtered_chat.txt")

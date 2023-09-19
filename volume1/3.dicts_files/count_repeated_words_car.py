class CountWordOcurrences:

# Write a program that reads a list of words from a file words.txt and finds how many times each word is contained in another
# file test.txt. The result should be written in the file result.txt, and the number of their ocurrences should sort in descending
# order. Handle all possible exceptions in your methods

    def read_words_to_count(file_path):
        # read a file an separate it by words
        try:
            with open(file_path, "r") as file:
                words = file.read().split()
            return words
        except FileNotFoundError:
            raise Exception(f"File not found: {file_path}")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {str(e)}")
        
    def count_unique_words(words):
        # return a dict with the words and the number of times every word appears
        try:
            word_counter = {}
            # iterate every word in words.txt
            for word in words:
                if word in word_counter:
                    # increase the value each time the word matches
                    word_counter[word]+=1
                else:
                    # set value to 1 if the word is not in the dict 
                    word_counter[word]=1        
            return word_counter
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {str(e)}")

    def count_words_repetition(words_to_count, words_counter):
        # return how many times a word in the original file exist in the second one
        try:
            counter_word_repitition={}
            # set of unique words in the original file
            unique_words = set(words_to_count)
            for word in unique_words:
                if word in words_counter:
                    # if the word exists on the second file the counter is set to the current key:'word'
                    counter_word_repitition[word]=words_counter[word]
                else:
                    # if not the counter is set to 0
                    counter_word_repitition[word]=0          
            return counter_word_repitition
              
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def order_word_counter_repetition(word_counter_repetition):
        sorted_results = sorted(word_counter_repetition.items(), key=lambda x: x[1], reverse=True)
        return sorted_results

    def write_a_file(filepath, times_each_word_exist):
        try:
            with open(filepath, "w") as outfile:
                for word, count in times_each_word_exist:
                    outfile.write(f'{word}: {count}\n')
                print(f"Filtered content saved to '{filepath}'.")

        except FileNotFoundError:
            print(f'File not found. {filepath}')
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__== "__main__":
    words_in_init_file = CountWordOcurrences.read_words_to_count("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/words.txt")
    words_in_test_file = CountWordOcurrences.read_words_to_count("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/test.txt")
    
    word_counter= CountWordOcurrences.count_unique_words(words_in_test_file)
    # for key, value in word_counter.items():
    #     print(f'key: {key}, value: {value}')

    counter_word_repitition = CountWordOcurrences.count_words_repetition(words_in_init_file, word_counter)
    # for key, value in counter_word_repitition.items():
    #     print(f'key: {key}, value: {value}')

    sorted_counter = CountWordOcurrences.order_word_counter_repetition(counter_word_repitition)
    CountWordOcurrences.write_a_file("/Users/carolinamachado/Documents/Development/DataStructuresPython/volume1/3.dicts_files/result.txt",
                                      sorted_counter)

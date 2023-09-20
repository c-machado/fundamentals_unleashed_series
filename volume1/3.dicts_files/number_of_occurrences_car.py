# write a program that counts the number of occurrences of each value in a given array of double values. use a dictionary 

class NumberOfOccurrences:

    def count_number_of_ocurrences(self, array_double_values):
        dict_cont={}
        for num in array_double_values:
            # check if the current number is in the dictionary, if so increase the counter by 1, otherwise set the counter to 1
            # the key is the number, the value is the counter
            if num in dict_cont:
                dict_cont[num]+=1
            else:
                dict_cont[num]=1
    
        return dict_cont

if __name__ == "__main__":
    array = [3,4,4,2.5,3,3,4,3,2.5]
    etst = NumberOfOccurrences().count_number_of_ocurrences(array)
    for key, value in etst.items():
        print(f'number: {key}, counter: {value}')


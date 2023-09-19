class NumberOfOccurrences:

    def count_number_of_ocurrences(self, array_double_values):
        dict_cont={}
        for num in array_double_values:
            if num in dict_cont:
                dict_cont[num]+=1
            else:
                dict_cont[num]=1
    
        return dict_cont

if __name__ == "__main__":
    array = [3,4,4,2.5,3,3,4,3,2.5]
    etst = NumberOfOccurrences().count_number_of_ocurrences(array)
    for key, value in etst.items():
        print(key,value)
import array as arr

class arrayListExample:

    def array_example():
        int_arr = arr.array('b',[])
        for i in range(20):
            num = i+1*5
            int_arr.append(num)
        print(f' the final array is: {int_arr}')

    def list_example():
        int_list = []
        for i in range (20):
            num = i+1 * 5
            int_list.append(num)
        print(f' the final list is: {int_list}')
     
    array_example()
    list_example()

import random
from datetime import date

class volume1:

    def interchange_integers(num1, num2):
        if (num1>num2):
            num_temp = num2
            num2=num1
            num1=num_temp
            print(f'num1: {num1}, num2; {num2}')
        else:
            print(f'num1: {num1}, num2; {num2}')

    def greatest_number(num1, num2):
        if num1>num2:
            return num1
        else:
            return num2

    def random_num():
        for i in range(10):
            num = random.randrange(100,200)
            print(f'the random number is: {num}')
        print(f'today is: {date.today()}')

    random_num()


    # print(greatest_number(2,3))
    # interchange_integers(4,3)
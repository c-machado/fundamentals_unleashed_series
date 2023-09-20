# write a program that prints from a given array of integers all numbers divisible by 3 and 7 using a lambda expression

numbers = [3, 7, 21, 20, 30, 90, 121]


divisibles_by_3 = filter(lambda number: number%3==0, numbers)
for number in divisibles_by_3:
    print(f'divisible by 3 {number}')

divisibles_by_7 = filter(lambda number: number%7==0, numbers)
for number in divisibles_by_7:
    print(f'divisible by 7 {number}')

divisible_by_3_and_7 = filter(lambda number: (number%3==0 and number%7==0), numbers)
for number in divisible_by_3_and_7:
    print(f'divisible by 3 and 7 {number}')


import pandas as pd

numbers = [3, 7, 21, 20, 30, 90, 121]

data = pd.DataFrame({'Numbers': numbers})

divisibles_by_3_and_7 = data.query('Numbers % 3 == 0 and Numbers % 7 == 0')

print(divisibles_by_3_and_7)
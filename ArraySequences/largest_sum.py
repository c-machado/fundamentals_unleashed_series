
def sum_array(arr):
    sum = 0
    array_sums = []
    for i in range(0, len(arr)):
        sum += arr[i]
        array_sums.append(sum)
    print(array_sums)
    largest = largest_sum(array_sums)
    return largest

def largest_sum(arr_sum):
    largest = float("-inf")
    for n in arr_sum:
        if n > largest:
            largest = n
    return largest


array = [-1, -2, -1, -3, -4, -10, -10]
sum = sum_array(array)
print(sum)


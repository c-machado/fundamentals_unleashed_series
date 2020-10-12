import random


def finder(array_to_shuffle):
    random.shuffle(array_to_shuffle)
    count = {}
    for num in array_to_shuffle:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    print(count)

    array_to_shuffle.remove(random.choice(array_to_shuffle))
    print(array_to_shuffle)

    for num in array_to_shuffle:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    print(count)
    deleted_num = count[1]
    print(deleted_num)
    return deleted_num

second_array = finder([1, 2, 3, 4, 5, 6, 7])





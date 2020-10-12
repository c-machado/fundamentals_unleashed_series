
def pair_sum(array, k):
    if len(array) < 2:
        return
    #sets for tracking
    seen = set()
    output = set()

    #for every number in array
    for num in array:
        #set target difference
        target = k - num

        #add it to set if target has not been seen
        if target not in seen:
            seen.add(num)

        else:
            #add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))

pair_sum([2, 1, 1, 2, 3, 0],4)






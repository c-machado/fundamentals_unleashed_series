import copy

student_name_list = ['Rene', 'Joseph', 'Janet', 'Jonas', 'Helen', 'Virginia']

# temp has a reference to the same element that exists on student_name_list
temp = student_name_list[2:3]
#print(temp)

primes = [2, 3, 5, 7, 11, 13, 17, 19]
# copy to reference the same objects of primes list
temp = primes[3:6]
# print(temp)
# update the reference to a new object
temp[2] = 15
# print(temp)
# print(primes)

# new list with copy the new elements
temp_deep_copy = copy.deepcopy(primes)
temp_deep_copy[2] = 88
print(temp_deep_copy)
print(primes)

# eight cells references to the same object
counters = [0] * 8
print(counters)

# it does not change the default value(0), it computes as a new integer
counters[2] += 1
print(counters)

# 'primes' is just receives references to the values on list 'extras'
extras = [23, 29, 31]
primes.extend(extras)
print(primes)
    
primes.append(99)
print(primes)

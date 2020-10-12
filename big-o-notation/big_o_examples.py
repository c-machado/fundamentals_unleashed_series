# This function is constant because regardless of the list size, the function will only ever take a constant step size,
def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    print(values[0])


# This function runs in O(n) (linear time). This means that the number of operations taking place scales linearly
# with n, so we can see here that a list of n values will print n times.
def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print(val)


# Note how we now have two loops, one nested inside another. This means that for a list of n items, we will have to
# perform n operations for every item in the list! This means in total, we will perform n times n assignments, or n^2.
def func_quad(lst):
    '''
    Prints pairs for every item in list.
    '''
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)


lst = [0, 1, 2, 3]
func_lin(lst)
func_constant(lst)
func_quad(lst)



import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0  # count actual elements (0 by default)
        self.capacity = 1  # default capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # Return the number of elements sorted in array
        return self.n

    def __getitem__(self, k):

        if not 0 <= k < self.n:
           return IndexError('k is out of bounds')  # check if K is out of the bounds in the array
        return self.A[k]  # retrieve from array at index k

    def append(self, ele):
        """
        Add element to the end of the array
        :param self:
        :param ele:
        :return:
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)  # 2x if capacity is not enough

        self.A[self.n] = ele # Set self.n index to element
        self.n +=1

    def _resize(self, new_cap):

        B = self.make_array(new_cap)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()


arr = DynamicArray()
arr.append(1)
arr.append(2)

len(arr)
print(len(arr))
print(arr[0])




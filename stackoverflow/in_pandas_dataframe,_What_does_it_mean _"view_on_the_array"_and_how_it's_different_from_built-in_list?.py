import numpy as np


# when slicing in the built-in list it creates a copy.

l = [0, 1, 2, 3, 4]
list2 = l[1:3]
list2[0] = 10
print(l)    # this returns [0, 1, 2, 3, 4]


# when slicing in nd.array doesn't create a new copy but it still referring to original array.

arr = np.array([0, 1, 2, 3, 4])
arr2 = arr[1:3]
arr2[0] = 10
print(arr)   # this returns [0,10,20,3,4]

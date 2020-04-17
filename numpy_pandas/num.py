# -*- coding: utf-8 -*-

import numpy as np

print(np.arange(10)) #creates an arryay 0f 0 to 9 elements

print(np.arange(1,10))

print(np.arange(1,10,2)) #odd numbers

print(np.arange(1,10,0.5))

print(np.arange(1,10,dtype='float64'))

arr = np.arange(1,10)

print(arr)

print(arr.ndim)

print(arr.shape)

print(arr.size)
print(arr.dtype)
print(arr.itemsize)

print(arr.itemsize * arr.size)

print(np.asarray([1,2,3,4,5]))
list2d = [[1,2,3],[4,5,6]]

arr2d = np.asarray(list2d)

print(arr2d)
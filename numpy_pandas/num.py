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


listzeros = np.zeros((3,4), dtype='int32')

print(listzeros)

np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)

print(np.random.random((3,4)))


rarr = np.random.random((3,4))

np.max(rarr, axis=0)
np.max(rarr, axis=1)

np.min(rarr, axis=0)
np.min(rarr, axis=1)

np.median(rarr, axis=0)
np.median(rarr, axis=1)

# Reshaping
# np.reshape(a, newshape, order='C')
new_rarr = np.reshape(rarr, (12,))
new_rarr = np.reshape(rarr, (12,1))

# Slicing
rarr = np.random.random((4,5))

rarr[:,:]
rarr[1:3,:]

rarr[:,1:]
rarr[:,1:3]

rarr[1:3,1:3]

rarr[[0,3],:]
rarr[:,[0,3]]


rarr[:-1,:]
rarr[-1:,:]



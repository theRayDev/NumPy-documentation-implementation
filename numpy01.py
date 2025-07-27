# example 1 - with average spped of 20ms
a = [1,2,3]
b = [4,5,6]
#c = []
#for i in range(0,len(a)):
#    c.append(a[i]*b[i])
#print(c)

# example 1 (using NumPy)
import numpy as np
array1 = np.array(a)
array2 = np.array(b)

c = array1*array2

print(c)

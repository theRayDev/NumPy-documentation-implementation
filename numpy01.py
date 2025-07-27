# example 1 - with average speed of 20ms
a = [1,2,3]
b = [4,5,6]
#c = []
#for i in range(0,len(a)):
#    c.append(a[i]*b[i])
#print(c)

# example 1 (using NumPy) - takes avg 150ms *Probably cuz of complexity of log n and for loop of py is of complexity n* - conclusion small sample size
''' NumPy is optimized for large-scale numerical operations through
vectorized C implementations.For very small arrays, Python loops may
appear faster due to lower overhead.However, for larger arrays,
NumPy significantly outperforms native Python due to efficient memory
access and vectorized computation. Both approaches have linear time 
complexity (O(n)).'''
import numpy as np
array1 = np.array(a)
array2 = np.array(b)

c = array1*array2

print(c)

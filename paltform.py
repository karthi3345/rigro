#1 Dimensional Array
#2 Dimensional Array
#3 Dimensional Array

import paltform as np
# A = np.array(5)
# np.ndim(A) #np.ndim() function returns the number of dimensions of the array
# #return 0
one = np.array([1,2,3,4,5])
np.ndim(one)
#return 1
two = np.array([[1,2,3],[4,5,6]])
np.ndim(two)
#return 2
three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
np.ndim(three)
#return 3
print("hello")
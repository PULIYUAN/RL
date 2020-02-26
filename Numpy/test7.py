import numpy as np

#----------------赋值的关联性---------------------------

#= 的赋值方式会带有关联性
a = np.arange(4)	# array([0, 1, 2, 3])
b = a
c = a
d = b
#改变a的第一个值，b、c、d的第一个值也会同时改变。
a[0] = 11
print(a)	# array([11,  1,  2,  3])
b is a  # True
c is a  # True
d is a  # True
#同样更改d的值，a、b、c也会改变。
d[1:3] = [22, 33]   # array([11, 22, 33,  3])
print(a)            # array([11, 22, 33,  3])
print(b)            # array([11, 22, 33,  3])
print(c)            # array([11, 22, 33,  3])

#copy() 的赋值方式没有关联性
d = a.copy()    # deep copy
print(d)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(d)        # array([11, 22, 33,  3])

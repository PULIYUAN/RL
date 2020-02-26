import numpy as np

#----------------Numpy array 分割---------------------------
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]])
"""
#横向分割
print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), 
 array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""

#纵向分割
print(np.split(A, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]

#错误分割
#print(np.split(A, 3, axis=1))
# ValueError: array split does not result in an equal division

#不等量分割 np.array_split()
print(np.array_split(A, 3, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), 
array([[ 2],
        [ 6],
        [10]]), 
array([[ 3],
        [ 7],
        [11]])]
"""

#其他分割方法：np.vsplit()、np.hsplit()
print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""

import numpy as np

#----------------Numpy array 合并---------------------------
#----------------序列合并-------------
#np.vstack() 上下合并
A = np.array([1,1,1])   #只是序列（只有一个[ ]）
B = np.array([2,2,2])  
print(np.vstack((A,B)))    # vertical stack
"""
[[1,1,1]
 [2,2,2]]
"""
C = np.vstack((A,B))      
print(A.shape,C.shape)    # (3,) (2,3)  此时A只是一个有3个元素的序列

#np.hstack() 左右合并
D = np.hstack((A,B))       # horizontal stack
print(D)# [1,1,1,2,2,2]
print(A.shape,D.shape)	# (3,) (6,)
#注意：序列不可转置

#----------------矩阵合并-------------
#np.newaxis() 维度增加 
print(A[np.newaxis,:])	# [[1 1 1]] 在行上加维度
print(A[np.newaxis,:].shape)	# (1,3)
print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""
print(A[:,np.newaxis].shape)	# (3,1)
#矩阵合并
a = np.array([1,1,1])[:,np.newaxis]
b = np.array([2,2,2])[:,np.newaxis]
c = np.vstack((a,b))   # vertical stack
d = np.hstack((a,b))   # horizontal stack
print(c)
"""
[[1]
...
[2]]
"""
print(d)
"""
[[1 2]
[1 2]
[1 2]]
"""
print(a.shape,d.shape)
# (3,1) (3,2)

#np.concatenate() →方便
e = np.concatenate((a,b,b,a),axis=0)
print(e)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""
f = np.concatenate((a,b,b,a),axis=1)
print(f)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""

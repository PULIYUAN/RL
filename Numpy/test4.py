import numpy as np

#----------------Numpy索引（从0开始）---------------------------
#一维索引
A = np.arange(3,15)
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])   
print(A[3])    # 6

#二维索引
B = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""     
print(B[2])         # [11 12 13 14] 第三行
print(B[1][1])      # 8
print(B[1, 1])      # 8
print(B[2,:])       #第3行
print(B[:,1])		#第2列
print(B[1, 1:3])    # [8 9] 切片操作

#for循环
for row in B:
    print(row)
"""    
[ 3,  4,  5, 6]
[ 7,  8,  9, 10]
[11, 12, 13, 14]
"""
for column in B.T:  #通过转置实现列的迭代
    print(column)
"""  
[ 3,  7,  11]
[ 4,  8,  12]
[ 5,  9,  13]
[ 6, 10,  14]
"""

#迭代输出
#flatten()：将多维的矩阵进行展开成1行的数列      
print(A.flatten())   
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
for item in A.flat:
    print(item)
# 3
# 4
#……
# 14

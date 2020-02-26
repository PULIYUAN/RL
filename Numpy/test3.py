import numpy as np

#----------------Numpy基础运算2---------------------------

#元素索引查找
A = np.arange(2,14).reshape((3,4)) 
# array([[ 2, 3, 4, 5]
#        [ 6, 7, 8, 9]
#        [10,11,12,13]])       
print(np.argmin(A))    # 0
print(np.argmax(A))    # 11

#均值、中位数计算   可加axis
print(np.mean(A))        # 7.5
print(np.average(A))     # 7.5
print(A.mean())          # 7.5
print(np.median(A))       # 7.5

#累和运算：原矩阵首项累加到对应项的元素之和
print(np.cumsum(A)) # [2 5 9 14 20 27 35 44 54 65 77 90]
#累差运算
print(np.diff(A))    
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]

#nonzero():将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵。
print(np.nonzero(A))    
# (array([0,0,0,0,1,1,1,1,2,2,2,2]),array([0,1,2,3,0,1,2,3,0,1,2,3]))

#排序
B = np.arange(14,2, -1).reshape((3,4)) 
# array([[14, 13, 12, 11],
#       [10,  9,  8,  7],
#       [ 6,  5,  4,  3]])
print(np.sort(A))    #逐行排序
# array([[11,12,13,14]
#        [ 7, 8, 9,10]
#        [ 3, 4, 5, 6]])

#转置
print(np.transpose(B))    
print(B.T)
# array([[14,10, 6]
#        [13, 9, 5]
#        [12, 8, 4]
#        [11, 7, 3]])

#clip():clip(Array,Array_min,Array_max)  判断矩阵中元素是否有比最小值小的或者比最大值大的元素，并将这些指定的元素转换为最小值或者最大值
print(np.clip(B,5,9))    
# array([[ 9, 9, 9, 9]
#        [ 9, 9, 8, 7]
#        [ 6, 5, 5, 5]])

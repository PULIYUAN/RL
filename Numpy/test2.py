import numpy as np

#----------------Numpy基础运算---------------------------
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])

c=a-b  # array([10, 19, 28, 37])
d=a+b   # array([10, 21, 32, 43])
e=a*b   # array([  0,  20,  60, 120])   逐个相乘
f=b**2  # array([0, 1, 4, 9])

#利用numpy中的数学工具
g=10*np.sin(a)  # array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])

#逻辑判断
print(b<3)  # array([ True,  True,  True, False], dtype=bool)

#二维矩阵乘法
aa=np.array([[1,1],[0,1]])
bb=np.arange(4).reshape((2,2))
c_dot = np.dot(a,b) #点乘
c_dot_2 = a.dot(b)
# array([[2, 4],
#       [2, 3]])

#sum(), min(), max()
cc = np.random.random((2,4))
print(cc)
# array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
#       [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])
np.sum(cc)   # 4.4043622002745959
np.min(cc)   # 0.23651223533671784
np.max(cc)   # 0.90438450240606416
#增加axis (axis=1行，axis=0列)
print("cc =",cc)
# a = [[ 0.23651224  0.41900661  0.84869417  0.46456022]
# [ 0.60771087  0.9043845   0.36603285  0.55746074]]
print("sum =",np.sum(cc,axis=1))
# sum = [ 1.96877324  2.43558896]
print("min =",np.min(cc,axis=0))
# min = [ 0.23651224  0.41900661  0.36603285  0.46456022]
print("max =",np.max(cc,axis=1))
# max = [ 0.84869417  0.9043845 ]







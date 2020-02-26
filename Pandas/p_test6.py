#----------------Pandas 合并 concat----------------------
#concat:简单合并
import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

#axis：合并方向  （默认：axis=0）
res = pd.concat([df1, df2, df3], axis=0) 
print(res)
'''
       a    b    c    d
 0  0.0  0.0  0.0  0.0
 1  0.0  0.0  0.0  0.0
 2  0.0  0.0  0.0  0.0
 0  1.0  1.0  1.0  1.0
 1  1.0  1.0  1.0  1.0
 2  1.0  1.0  1.0  1.0
 0  2.0  2.0  2.0  2.0
 1  2.0  2.0  2.0  2.0
 2  2.0  2.0  2.0  2.0
'''
#结果的index是0, 1, 2, 0, 1, 2, 0, 1, 2

#ignore_index：重置 index 
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)
print(res)
'''
     a    b    c    d
 0  0.0  0.0  0.0  0.0
 1  0.0  0.0  0.0  0.0
 2  0.0  0.0  0.0  0.0
 3  1.0  1.0  1.0  1.0
 4  1.0  1.0  1.0  1.0
 5  1.0  1.0  1.0  1.0
 6  2.0  2.0  2.0  2.0
 7  2.0  2.0  2.0  2.0
 8  2.0  2.0  2.0  2.0
'''

#join ：合并方式  （默认：join='outer'）
df4 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

#纵向"外"合并df4与df5
#依照column来做纵向合并，有相同的column上下合并在一起，其他独自的column个自成列
res = pd.concat([df4, df5], axis=0, join='outer')
print(res)
#     a    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN
# 2  0.0  0.0  0.0  0.0  NaN
# 3  0.0  0.0  0.0  0.0  NaN
# 2  NaN  1.0  1.0  1.0  1.0
# 3  NaN  1.0  1.0  1.0  1.0
# 4  NaN  1.0  1.0  1.0  1.0

#纵向"内"合并df4与df5
#只有相同的column合并在一起，其他的会被抛弃
res = pd.concat([df4, df5], axis=0, join='inner')
print(res)
#     b    c    d
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  0.0  0.0
# 2  1.0  1.0  1.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
res = pd.concat([df4, df5], axis=0, join='inner', ignore_index=True)
print(res)
#     b    c    d
# 0  0.0  0.0  0.0
# 1  0.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  1.0  1.0  1.0
# 4  1.0  1.0  1.0
# 5  1.0  1.0  1.0

#join_axes ：依照 axes 合并
#依照`df4.index`进行横向合并
res = pd.concat([df4, df5], axis=1, join_axes=[df4.index])
print(res)
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0

#移除join_axes，并打印结果
res = pd.concat([df4, df5], axis=1)
print(res)
#     a    b    c    d    b    c    d    e
# 1  0.0  0.0  0.0  0.0  NaN  NaN  NaN  NaN
# 2  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 3  0.0  0.0  0.0  0.0  1.0  1.0  1.0  1.0
# 4  NaN  NaN  NaN  NaN  1.0  1.0  1.0  1.0

#append ：添加数据
#定义资料集
df6 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df7 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df8 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

#将df7合并到df6的下面，以及重置index，并打印出结果
res = df6.append(df7, ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0

#合并多个df，将df7与df8合并至df6的下面，以及重置index，并打印出结果
res = df6.append([df7, df8], ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  1.0  1.0  1.0
# 4  1.0  1.0  1.0  1.0
# 5  1.0  1.0  1.0  1.0
# 6  1.0  1.0  1.0  1.0
# 7  1.0  1.0  1.0  1.0
# 8  1.0  1.0  1.0  1.0

#合并series，将s1合并至df6，以及重置index，并打印出结果
res = df6.append(s1, ignore_index=True)
print(res)
#     a    b    c    d
# 0  0.0  0.0  0.0  0.0
# 1  0.0  0.0  0.0  0.0
# 2  0.0  0.0  0.0  0.0
# 3  1.0  2.0  3.0  4.0

#----------------Pandas 合并 merge-------------------------
#merge：用于两组有key column的数据,统一索引的数据（两组数据有相同关键字）
import pandas as pd

#依据一组key合并
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
print(left)
'''
    A   B key
 0  A0  B0  K0
 1  A1  B1  K1
 2  A2  B2  K2
 3  A3  B3  K3
'''
print(right)
'''
    C   D key
 0  C0  D0  K0
 1  C1  D1  K1
 2  C2  D2  K2
 3  C3  D3  K3
'''
#依据key column合并，并打印出
res = pd.merge(left, right, on='key')
print(res)
'''
     A   B key   C   D
 0  A0  B0  K0  C0  D0
 1  A1  B1  K1  C1  D1
 2  A2  B2  K2  C2  D2
 3  A3  B3  K3  C3  D3
'''

#依据两组key合并:合并时有4种方法how = ['left', 'right', 'outer', 'inner']，预设值how='inner'
left_ = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right_ = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
print(left_)
'''
    A   B key1 key2
 0  A0  B0   K0   K0
 1  A1  B1   K0   K1
 2  A2  B2   K1   K0
 3  A3  B3   K2   K1
'''
print(right_)
'''
    C   D key1 key2
 0  C0  D0   K0   K0
 1  C1  D1   K1   K0
 2  C2  D2   K1   K0
 3  C3  D3   K2   K0
'''
#依据key1与key2 columns进行合并，并打印出四种结果['left', 'right', 'outer', 'inner']
res = pd.merge(left_, right_, on=['key1', 'key2'], how='inner')
print(res)
'''
    A   B key1 key2   C   D
 0  A0  B0   K0   K0  C0  D0
 1  A2  B2   K1   K0  C1  D1
 2  A2  B2   K1   K0  C2  D2
'''
res = pd.merge(left_, right_, on=['key1', 'key2'], how='outer')
print(res)
'''
     A    B key1 key2    C    D
 0   A0   B0   K0   K0   C0   D0
 1   A1   B1   K0   K1  NaN  NaN
 2   A2   B2   K1   K0   C1   D1
 3   A2   B2   K1   K0   C2   D2
 4   A3   B3   K2   K1  NaN  NaN
 5  NaN  NaN   K2   K0   C3   D3
'''
res = pd.merge(left_, right_, on=['key1', 'key2'], how='left')
print(res)
'''
    A   B key1 key2    C    D
 0  A0  B0   K0   K0   C0   D0
 1  A1  B1   K0   K1  NaN  NaN
 2  A2  B2   K1   K0   C1   D1
 3  A2  B2   K1   K0   C2   D2
 4  A3  B3   K2   K1  NaN  NaN
'''
res = pd.merge(left, right, on=['key1', 'key2'], how='right')
print(res)
'''
     A    B key1 key2   C   D
 0   A0   B0   K0   K0  C0  D0
 1   A2   B2   K1   K0  C1  D1
 2   A2   B2   K1   K0  C2  D2
 3  NaN  NaN   K2   K0  C3  D3
'''

#Indicator :indicator=True将合并的记录放在新的一列
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
'''
   col1 col_left
 0     0        a
 1     1        b
'''
print(df2)
'''
   col1  col_right
 0     1          2
 1     2          2
 2     2          2
'''
# 依据col1进行合并，并启用indicator=True，最后打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(res)
'''
   col1 col_left  col_right      _merge
 0   0.0        a        NaN   left_only
 1   1.0        b        2.0        both
 2   2.0      NaN        2.0  right_only
 3   2.0      NaN        2.0  right_only
'''
# 自定indicator column的名称，并打印出
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)
'''
   col1 col_left  col_right indicator_column
 0   0.0        a        NaN        left_only
 1   1.0        b        2.0             both
 2   2.0      NaN        2.0       right_only
 3   2.0      NaN        2.0       right_only
'''

#依据index合并
_left_ = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
_right_ = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])
print(_left_)
'''
     A   B
 K0  A0  B0
 K1  A1  B1
 K2  A2  B2
'''
print(_right_)
'''
     C   D
 K0  C0  D0
 K2  C2  D2
 K3  C3  D3
'''
#依据左右资料集的index进行合并，how='outer',并打印出
res = pd.merge(_left_, _right_, left_index=True, right_index=True, how='outer')
print(res)
'''
      A    B    C    D
 K0   A0   B0   C0   D0
 K1   A1   B1  NaN  NaN
 K2   A2   B2   C2   D2
 K3  NaN  NaN   C3   D3
'''
#依据左右资料集的index进行合并，how='inner',并打印出
res = pd.merge(_left_, _right_, left_index=True, right_index=True, how='inner')
print(res)
'''
     A   B   C   D
 K0  A0  B0  C0  D0
 K2  A2  B2  C2  D2
'''

#解决overlapping的问题 
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
#使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)
'''
    age_boy   k  age_girl
 0        1  K0         4
 1        1  K0         5
'''

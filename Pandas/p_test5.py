#----------------Pandas 导入导出----------------------
#pandas可以读取与存取的资料格式：csv、excel、json、html与pickle等
#读取函数：read_csv/excel
#格式转换：to_csv/excle
import pandas as pd 

#读取csv
data = pd.read_csv('student.csv')
print(data)

#将资料存取成pickle
#data.to_pickle('student.pickle')

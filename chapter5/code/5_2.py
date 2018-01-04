<<<<<<< HEAD
# import pandas as pd
# filename = '../data/sales_data.xls'
# data = pd.read_excel(filename,index_col = u'序号')

# print(data)
# data[data == u'好'] = 1
# data[data == u'是'] = 1
# data[data == u'高'] = 1
# data[data != 1 ] = -1
# x = data.iloc[:,:3].as_matrix().astype(int)
# y = data.iloc[:,3].as_matrix().astype(int)


import math 
x = 0
for i in range(30):
	print(x)
	x = math.acos(x/2)
	
	
=======
import pandas as pd

filename = '../data/sales_data.xls'
data = pd.read_excel(filename,index_col=u'序号')

data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1

x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion = 'entropy')
dtc.fit(x,y)

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("tree.dot","w") as f:
	f = export_graphviz(dtc,feature_names=data.columns,out_file=f)


>>>>>>> 499749e1b2d3b40ba5ad57a370a84e70c21ab53c





import pandas as pd

datafile = '../data/discretization_data.xls'
data = pd.read_excel(datafile)
data = data[u'肝气郁结证型系数'].copy()
k=4
print(data)
dl = pd.cut(data,k,labels=range(k))
w = [1.0*i/k for i in range(k+1)]

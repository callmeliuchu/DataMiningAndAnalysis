import pandas as pd
from scipy.interpolate import lagrange


inputfile = '../data/missing_data.xls'
outputfile = '../tmp/missing_data_processed.xls'




data = pd.read_excel(inputfile,header=None)

def ployinterp_column(s,n,k=5):
	y = s[list(range(n-k,n))+list(range(n,n+k+1))]
	y = y[y.notnull()]
	return lagrange(y.index,list(y))(n)


for i in data.columns:
	for j in range(len(data)):
		if (data[i].isnull())[j]:
			data[i][j] = ployinterp_column(data[i],j)

print(data)
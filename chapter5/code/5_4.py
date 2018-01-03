import pandas as pd
inputfile = '../data/consumption_data.xls'
outputfile = '../tmp/data_type.xls'
k = 3
iteration = 500
data = pd.read_excel(inputfile,index_col = 'Id')
data_zs = 1.0*(data - data.mean())/data.std()
# print(data_zs)

from sklearn.cluster import KMeans
model = KMeans(n_clusters=k,n_jobs=1,max_iter=iteration)
model.fit(data_zs)

print(model.labels_)
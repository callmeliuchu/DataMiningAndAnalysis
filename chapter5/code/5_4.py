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

r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
print(r1)
print(r2)
r = pd.concat([r2,r1],axis=1)
print(r)

r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
print(r)
r.columns = list(data.columns) + [u'聚类类别']
# r.to_excel(outputfile)

print(len(data.iloc[0]))





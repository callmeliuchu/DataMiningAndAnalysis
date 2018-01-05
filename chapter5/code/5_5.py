import pandas as pd
inputfile = '../data/consumption_data.xls'
outputfile = '../tmp/data_type.xls'
k = 3
iteration = 500
data = pd.read_excel(inputfile,index_col = 'Id')
data_zs = 1.0*(data - data.mean())/data.std()


from sklearn.cluster import KMeans
model = KMeans(n_clusters=k,n_jobs=1,max_iter=iteration)
model.fit(data_zs)


r1 = pd.Series(model.labels_).value_counts()
r2 = pd.DataFrame(model.cluster_centers_)
r = pd.concat([r2,r1],axis=1)

r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
r.columns = list(data.columns) + [u'聚类类别']
from sklearn.manifold import TSNE

tsne = TSNE()
tsne.fit_transform(data_zs)
tsne = pd.DataFrame(tsne.embedding_,index=data_zs.index)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

d = tsne[r[u'聚类类别'] == 0] 
plt.plot(d[0],d[1],'r.')
d = tsne[r[u'聚类类别'] == 1] 
plt.plot(d[0],d[1],'go')
d = tsne[r[u'聚类类别'] == 2] 
plt.plot(d[0],d[1],'b*')
plt.show()

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
r = pd.concat([r2,r1],axis=1)
print(r)

# r = pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
# print(r)
r.columns = list(data.columns) + [u'聚类类别']
# r.to_excel(outputfile)

# print(len(data.iloc[0]))



def density_plot(data,title):
	import matplotlib.pyplot as plt
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False
	plt.figure()
	for i in range(len(data.iloc[0])):
		(data.iloc[:,i]).plot(kind='kde',label=data.columns[i],linewidth=2)
	plt.ylabel(u'密度')
	plt.xlabel(u'人数')
	plt.title(u'聚类类别%s个属性密度曲线' %title)
	plt.legend()
	return plt



pic_output = '../tmp/pd_'
for i in range(k):
	density_plot(data[r[u'聚类类别']==i],str(i)).savefig(u'%s%s.png' %(pic_output,i))











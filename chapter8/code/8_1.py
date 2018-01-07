from __future__ import print_function
import pandas as pd
from sklearn.cluster import KMeans


datafile = '../data/data.xls'
processdfile = '../tmp/data_processed.xls'

typelabels = {'肝气郁结证型系数': 'A', '肝肾阴虚证型系数': 'F', '气血两虚证型系数': 'D', '冲任失调证型系数': 'C', '热毒蕴结证型系数': 'B', '脾胃虚弱证型系数': 'E'}
k = 4

data = pd.read_excel(datafile)
keys = list(typelabels.keys())
result = pd.DataFrame()




if __name__ == '__main__':
	for i in range(len(keys)):
		print('now the processor %s is on' % keys[i])
		kmodel = KMeans(n_clusters=k,n_jobs=1)
		kmodel.fit(data[[keys[i]]].as_matrix())

		r1 = pd.DataFrame(kmodel.cluster_centers_,columns=[typelabels[keys[i]]])
		r2 = pd.Series(kmodel.labels_).value_counts()
		r2 = pd.DataFrame(r2,columns=[typelabels[keys[i]]+'n'])
		r = pd.concat([r1,r2],axis=1).sort(typelabels[keys[i]])
		r.index = [1,2,3,4]
		r[typelabels[keys[i]]] = pd.rolling_mean(r[typelabels[keys[i]]],2)
		r[typelabels[keys[i]]][1] = 0.0
		result = result.append(r.T)
result = result.sort()
result.to_excel(processdfile)

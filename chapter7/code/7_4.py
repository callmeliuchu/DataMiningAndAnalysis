import pandas as pd
from sklearn.cluster import KMeans

inputfile = '../tmp/zscoreddata.xls'
k = 5


data = pd.read_excel(inputfile)

kmodel = KMeans(n_clusters = k,n_jobs = 1)
kmodel.fit(data)

print(kmodel.cluster_centers_)
print(kmodel.labels_)
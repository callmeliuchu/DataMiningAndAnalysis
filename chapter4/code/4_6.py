import pandas as pd


inputfile = '../data/principal_component.xls'
outputfile = '../tmp/dimention_reducted.xls'

data = pd.read_excel(inputfile,header=None)

from sklearn.decomposition import PCA

pca = PCA(3)
pca.fit(data)
low_d = pca.transform(data)
kk = pca.inverse_transform(low_d)
print(kk)
# print(pca.explained_variance_ratio_)
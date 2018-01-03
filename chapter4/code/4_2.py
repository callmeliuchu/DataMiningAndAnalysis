import pandas as pd
import numpy as np

datafile = '../data/normalization_data.xls'
data = pd.read_excel(datafile,header=None)
print(data)
print((data-data.min())/(data.max()-data.min()))
print((data-data.mean())/data.std())
print(data/10**np.ceil(np.log10(data.abs().max())))
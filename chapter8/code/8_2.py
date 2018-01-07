from __future__ import print_function
import pandas as pd

from apriori import *
import time


inputfile = '../data/apriori.txt'
data = pd.read_csv(inputfile,header=None,dtype=object)
start = time.clock()
ct = lambda x:pd.Series(1,index=x[pd.notnull(x)])
b = map(ct,data.as_matrix())
data = pd.DataFrame(list(b)).fillna(0)
end = time.clock()
print(end-start)
del b


support = 0.06
confidence = 0.75
ms = '--------'


start = time.clock()
find_rule(data,support,confidence,ms)
end = time.clock()
print(end-start)


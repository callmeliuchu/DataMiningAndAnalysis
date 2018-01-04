import pandas as pd
inputfile = '../data/sales_data.xls'
data = pd.read_excel(inputfile,index_col=u'序号')
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = 0
x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)


from keras.models import Sequential
from keras.layers.core import Dense,Activation


model = Sequential()
model.add(Dense(3,10))
model.add(Activation('relu'))
model.add(Dense(10,1))
model.add(Activation('sigmoid'))
model.compile(loss = 'binary_crossentropy',optimazer='adam',class_mode='binary')

import pandas as pd
from random import shuffle

datafile = '../data/model.xls'
data = pd.read_excel(datafile)
data = data.as_matrix()
shuffle(data)
p = 0.8
train = data[:int(len(data)*p),:]
test = data[int(len(data)*p):,:]


# from keras.models import Sequential
# from keras.layers.core import Dense,Activation

# netfile = '../tmp/net.model'
# net = Sequential()
# net.add(Dense(3,10))
# net.add(Activation('relu'))
# net.add(Dense(10,1))
# net.add(Activation('sigmoid'))
# net.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')
# net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_size=1)
# net.save_weights(netfile)
# predict_result = net.predict_classes(train[:,:3]).reshape(len(train))


# from cm_plot import *
# cm_plot(train[:,3],predict_result).show()



from sklearn.tree import DecisionTreeClassifier

treefile = '../tmp/tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])

from sklearn.externals import joblib
joblib.dump(tree,treefile)


from cm_plot import *
cm_plot(train[:,3],tree.predict(train[:,:3])).show()





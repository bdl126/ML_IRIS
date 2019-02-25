import sys
sys.path.insert(0, "functions/")

import loadnformat as f
import ExtractData as ExD
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as AX
import makeplot as mp

dataFileDir = "IRIS_DATA/"
dataFileName = "iris.csv"

#chose data to compare
    #['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

x_name="sepal_length"
y_name="sepal_width"

#chose data to compare


dataset = f.load_csv(dataFileDir+dataFileName)
DataColumnName=dataset[0]


for column in range(len(dataset[0])-1):
    f.str_column_to_float(dataset, column)

label = f.str_column_to_integer(dataset, 4)

formData=ExD.ExData(dataset, label)
formData.extractTrainData(DataColumnName.index(x_name), DataColumnName.index(y_name))

X = np.array(formData.TrainSetosa + formData.TrainVirginica + formData.TrainVersicolor)
Y = np.array(formData.trainLabelSetosa + formData.trainLabelVirginica + formData.trainLabelVersicolor)
clf = SVC(kernel="rbf", C=2,degree=5)
clf.fit(X, Y)


data = (formData.TrainSetosa, formData.TrainVirginica, formData.TrainVersicolor)
groups = ("Setos", "Virginica","Versicolor")

# Create plot
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
xx, yy = mp.make_meshgrid(X, X)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(yy.shape)

t=0
for data, group in zip(data, groups):
    x, y = zip(*data)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(x, y, alpha=0.8, cmap=plt.cm.coolwarm, edgecolors='k', s=30, label=group)
    t=t+1

print(t)
plt.ylim(min(y)-1, max(y)+1)
plt.xlim(min(x)-1, max(x)+1)
plt.ylabel(y_name)
plt.xlabel(x_name)
plt.title('iris_map')
plt.legend(loc=2)
plt.show()




print(clf.predict([[4.6, 3.4]]))

print(DataColumnName)

print(formData.TrainVirginica)
print(label)
import sys
sys.path.insert(0, "functions/")

import loadnformat as f
import ExtractData as ExD
from sklearn.svm import SVC
import numpy as np
import matplotlib.pyplot as plt

dataFileDir = "IRIS_DATA/"
dataFileName = "iris.csv"

#chose data to compare
    #['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

x_name="sepal_length"
y_name="sepal_width"

#chose data to compare


dataset = f.load_csv(dataFileDir+dataFileName)
DataColumnName=dataset[0];


for column in range(len(dataset[0])-1):
    f.str_column_to_float(dataset, column)

label = f.str_column_to_integer(dataset, 4)

formData=ExD.ExData(dataset, label)
formData.extractTrainData(DataColumnName.index(x_name), DataColumnName.index(y_name))

X = np.array(formData.TrainSetosa + formData.TrainVirginica)
Y = np.array(formData.trainLabelSetosa + formData.trainLabelVirginica)
clf = SVC(kernel="linear")
clf.fit(X, Y)


xs = [x[0] for x in X]
ys = [x[1] for x in X]

data = (formData.TrainSetosa, formData.TrainVirginica)
colors = ("red", "green")
groups = ("Setos", "TrainVirginica")

# Create plot
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    plt.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

plt.ylabel(y_name)
plt.xlabel(x_name)
plt.title('iris_map')
plt.legend(loc=2)
plt.show()




print(clf.predict([[4.6, 3.4]]))

print(DataColumnName)

print(formData.TrainVirginica)
print(label)
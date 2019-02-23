import sys
sys.path.insert(0, "functions/")

import loadnformat as f
import numpy as np
import matplotlib.pyplot as plt

dataFileDir = "IRIS_DATA/"
dataFileName = "iris.csv"
dataset = f.load_csv(dataFileDir+dataFileName)

label = f.str_column_to_integer(dataset, 4)

print(dataset)
print(label)
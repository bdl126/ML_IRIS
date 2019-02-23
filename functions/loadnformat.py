from csv import reader


# Load a CSV file
def load_csv(filename):
    file = open(str(filename), "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_integer(dataset,column):
    list = []
    for row in dataset:
        list.append(row[column])
    tmp = set(list)
    dictio = dict()

    for i, value in enumerate(tmp):
        dictio[value] = i
    for row in dataset:
        row[column] = dictio[row[column]]
    return dictio
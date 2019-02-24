from csv import reader


# Load a CSV file
def load_csv(filename):
    file = open(str(filename), "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

def str_column_to_float(dataset, column):
    iterdata=iter(dataset)
    next(iterdata)
    for row in iterdata:
        row[column] = float(row[column].strip())

def str_column_to_integer(dataset,column):
    list = []
    iterdata = iter(dataset)
    next(iterdata)
    for row in iterdata:
        list.append(row[column])
    tmp = set(list)
    dictio = dict()

    for i, value in enumerate(tmp):
        dictio[value] = i

    iterdata = iter(dataset)
    next(iterdata)
    for row in iterdata:
        row[column] = dictio[row[column]]
    return dictio
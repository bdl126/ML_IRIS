class ExData:
    def __init__(self, dataset, label):
        self.label = label
        self.dataset = dataset

        self.Setosa      = []
        self.Virginica   = []
        self.Versicolor  = []

        self.TrainSetosa      = []
        self.TrainVirginica   = []
        self.TrainVersicolor  = []

        self.trainLabelSetosa=[]
        self.trainLabelVersicolor = []
        self.trainLabelVirginica = []



    def extractData(self):
        iterdata = iter(self.dataset)
        next(iterdata)
        for element in iterdata:
            if self.label['versicolor'] == element[4]:
                self.Versicolor.append(element)
            elif self.label['virginica'] == element[4]:
                self.Virginica.append(element)
            else:
                self.Setosa.append(element)

    def extractTrainData(self, element1, element2):
        iterdata = iter(self.dataset)
        next(iterdata)
        for element in iterdata:
            ltemp = []
            ltemp.append(element[element1])
            ltemp.append(element[element2])
            if self.label['versicolor'] == element[4]:
                self.TrainVersicolor.append(ltemp)
                self.trainLabelVersicolor.append(self.label['versicolor'])
            elif self.label['virginica'] == element[4]:
                self.TrainVirginica.append(ltemp)
                self.trainLabelVirginica.append(self.label['virginica'])
            else:
                self.TrainSetosa.append(ltemp)
                self.trainLabelSetosa.append(self.label['setosa'])

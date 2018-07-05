import csv
import numpy as np

class MesureRepository:

    def load(this,uri):
        with open("uri") as f:
         reader = csv.DictReader(f,delimiter=";")
         theoricals = []
         mesures = []

        for row in reader:
            theorical = float(row["good"])#identify the column
            mesure = float(row["bad"])
            theoricals.append(theorical)
            mesures.append(mesure)

#je veux mes courbes
    def getTheoricalList(this):
        return this.theoricals
    def getExperimentalList(this):
        return this.mesures
#je veux leur differences
    def getDifferenceErrorList(this):
        t = np.array(this.theoricals)
        m = np.array(this.mesures)
        return  m - t;

    def getQuadraticsErrorList(this):
        return np.square(this.getDifferenceErrorList())

#je veux mes les endroits ou mes list divergent selon leurs écrats
    def getTimeErrorLetList(this,l,delta):
        res=[]
        for i in range(0,len(l)):
            if l[i]>= delta:
                res.append(i)
        return res

    def getTimeDifferenceErrorList(this,delta):
       return this. getTimeErrorLetList(this,this.getTheoricalList(),delta)

    def getTimeQuadraticsErrorList(this,delta):
        return  this. getTimeErrorLetList(this,this.getQuadraticsErrorList(),delta)



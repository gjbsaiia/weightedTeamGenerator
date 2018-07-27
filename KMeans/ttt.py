import numpy as np
import sys
import os
import matplotlib.pyplot as mat
import csv
import math
import testv2

def read2d(filename):
    data = []
    file = open(filename, newline='')
    #lines = file.read().splitlines()
    reader = csv.reader(file, delimiter=' ',quotechar='|')
    for line in reader:
        linestring = ''.join(line)
        if('\"' in linestring):
            linestring = (list(s.replace(',','') for s in list(filter(None,linestring.split('\"')))))
        else:
            linestring = linestring.split(',')
        try:
            large=float(linestring[0])
            data.append((math.log(large),float(linestring[1])))
        except ValueError:
            print('NaN')
    print(data)
    print(len(data))
    return data



data = read2d('2D_data.csv')
larges = [i[0] for i in data]
ones=[]

mat.hist(larges, bins=20)
mat.show()

dataSplits = {}
infoSplits = {}
for i in range(len(data[0])):
    dataSplits[i]=[val[i] for val in data]
    infoSplits[i] = (np.average(dataSplits[i]),np.std(dataSplits[i]))
    dataSplits[i]=[(val[i]-infoSplits[i][0])/infoSplits[i][1] for val in data]
print(dataSplits)
print(infoSplits)






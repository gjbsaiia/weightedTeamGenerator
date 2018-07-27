import numpy as np
import sys
import os
import matplotlib.pyplot as mat
import csv
import math

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

            data.append((float(linestring[0]),float(linestring[1])))
        except ValueError:
            print('NaN')
    print(data)
    print(len(data))
    return data

def dataTransform(data=[1], type='log'):
    newData=[]
    if type == 'log':
        newData = [math.log(i) for i in data]
    elif type == 'sq':
        newData = [i**2 for i in data]
    elif type == 'sqrt':
        newData = [math.sqrt(i) for i in data]
    elif type == 'inv':
        newData = [1/i for i in data]
    elif type=='none':
        newData = data
    else:
        print('invalid type given, default is log')
    return newData

def zipData(datasets=[[1]]):
    data = []
    for x in range(len(datasets[0])):
        tuple = ()
        for i in range(len(datasets)):
            tuple = tuple+ (datasets[i][x],)
        data.append(tuple)
    return data

def dataZify(data):
        dataSplits = {}
        infoSplits = {}
        for i in range(len(data[0])):
            dataSplits[i] = [val[i] for val in data]
            infoSplits[i] = (np.average(dataSplits[i]), np.std(dataSplits[i]))
            dataSplits[i] = [(val[i] - infoSplits[i][0]) / infoSplits[i][1] for val in data]
        return (dataSplits),(infoSplits)

#def calcSigma(vector=[1], )







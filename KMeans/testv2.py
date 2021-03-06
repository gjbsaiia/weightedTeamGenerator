import numpy as np
import sys
import os
import matplotlib.pyplot as mat
#import operator
import csv
import dataUtil


FEATURES = 2

def sortify(centroids, dataCents):
    sortedCentroids = {}
    i=0
    swaps = {}
    while len(centroids) > 0:
        minimum = min(centroids.items(),key=lambda x:x[1])
        sortedCentroids[i]=minimum[1]
        centroids.pop(minimum[0])
        swaps[minimum[0]]=i
        i+=1

    dataCents = swapAssignments(dataCents,swaps)
    return sortedCentroids

def swapAssignments(dataCents, swaps):
    sortify
    newCents = []
    for d in dataCents:
        newCents.append(swaps[d])
    return newCents


#def initCentroids(numCentroids):
#    centroids = {}
#    for i in range(numCentroids):
#        centroids[i] = (int(np.random.binomial(11,.12)*100))
#    return centroids

def initCentroids(numCentroids, data):
	centroids = {}
	i=0
	while(len(centroids) < numCentroids):
		datapt = data[(int(np.random.rand(1)*len(data)))]
		if(datapt not in centroids.values()):
			centroids[i] = datapt
			i+=1
	return centroids


def nearestCentroid(centroids, datapt):
    nearest = -1
    nearestDist = sys.maxsize;
    for c in centroids:
        if(dist(centroids[c],datapt) < nearestDist):
            nearestDist = dist(centroids[c],datapt)
            nearest = c
    return nearest


def randData(amt):
    data = []
    for i in range(amt):
        data.append(tuple(np.random.normal(50, 10,FEATURES)))
    return data

def dist(c,d):
    if(type(c) != tuple or type(d) != tuple):
        print('make both inputs tuples')
        return -1
    if(len(c) != len(d)):
        print('make both tuples the same length')
        return -1
    dist = 0
    for i in range(len(c)):
        dist += (c[i]-d[i])**2
    return dist


def refactorCentroids(centroids,dataCents, data):
    i = 0
    newCentroids ={}
    for c in centroids:
        sum = (0,)*FEATURES
        count = 0
        j=0
        for d in data:
            if(dataCents[j] == i):
                sum = addtuples(sum,d)
                count+=1
            j+=1
        if(count > 0):
            newCentroids[i]=divtuples(sum,count)
        else:
            newCentroids[i]=centroids[i]
        i +=1
    return newCentroids

def addtuples(*args):
    return tuple(map(sum, zip(*args)))

def divtuples(val,divisor):
    return tuple(map(lambda x: x / divisor, val))


def checkCentroids(new,old):
    count = len(new)
    for c in old:
        if(old[c] == new[c]):
            count -=1

    if(count == 0):
        return True
    else:
        return False
def main(clust,data):
    origData = data
    larges = dataUtil.dataTransform(data=[i[0] for i in data], type='log')
    smalls = dataUtil.dataTransform(data=[i[1] for i in data], type='none')
    data = dataUtil.zipData(datasets=[larges, smalls])
    zdata, metad = dataUtil.dataZify(data)
    print('data metadata index: (avg, std): ')
    print(metad)
    data = dataUtil.zipData(datasets=[zdata[0],zdata[1]])
    centroids = initCentroids(clust,data)
    print('first centroids: ' + str(centroids))
    dataCents = []
    for d in data:
        dataCents.append(nearestCentroid(centroids, d))

    centroids = refactorCentroids(centroids, dataCents, data)
    print(centroids)
    notClose = True
    while(notClose):
        dataCents.clear()
        for d in data:
            dataCents.append(nearestCentroid(centroids, d))

        newCentroids = refactorCentroids(centroids, dataCents,data)
        if(checkCentroids(newCentroids,centroids)):
            notClose = False
        centroids = newCentroids

    print('\n\n')
    print('old dc: '+str(dataCents))
    print('final centroids: '+ str(centroids))
    print('data:           '+ str(data))
    print('data centroids: '+str(dataCents))
    ones = []
    print(centroids)
    for i in range(len(centroids)):
        ones.append(1)
    mores = []
    for j in range(len(data)):
        mores.append(1)

    min(centroids.items(), key=lambda x: x[1])
    totalErr = 0
    while(len(centroids)>0):
        minimum = min(centroids.items(),key=lambda x:x[1])
        centroids.pop(minimum[0])
        mat.scatter(minimum[1][0],minimum[1][1],s=30, color = (0,0,0))
        dataList = []
        i=0
        for d in dataCents:
            if(d == minimum[0]):
                dataList.append(data[i])
                totalErr += dist(data[i],minimum[1])
            i+=1
        print('num in cluster '+ str(minimum[0])+' located at: '+str(minimum[1])+' ::::: '+str(len(dataList)))
        mat.scatter([i[0] for i in dataList],[i[1] for i in dataList],s=4)
        mat.scatter(minimum[1][0], minimum[1][1], s=30, color=(0, 0, 0))

    mat.show()
    return totalErr/len(data)


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


if __name__ == '__main__':
    try:
        errs ={}
        # data = randData(1000)
        data = read2d('2D_data.csv')



        for i in range(1,8):
            errs[i] = main(i, data)
        mat.plot(errs.keys(),errs.values())
        mat.show()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

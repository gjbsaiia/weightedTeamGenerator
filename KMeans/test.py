import numpy as np
import sys
import os
import matplotlib.pyplot as mat
import operator

def readData(filename):
    readdata = []
    file = open(filename)
    lines = file.read().splitlines()
    for line in lines:
        try:
            readdata.append(float(line.split(',')[1]))
        except ValueError:
            print('none')

    return readdata

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


def initCentroids(numCentroids):
    centroids = {}
    for i in range(numCentroids):
        centroids[i] = (int(np.random.binomial(11,.12)*100))
    return centroids

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
    nearestDist = 1000000;
    for c in centroids:
        if(dist(centroids[c],datapt) < nearestDist):
            nearestDist = dist(centroids[c],datapt)
            nearest = c
    return nearest


def randData(amt):
    data = []
    for i in range(amt):
        data.append((np.random.normal(50, 10,1)))
    return data

def dist(c,d):
    return abs(c-d)

def refactorCentroids(centroids,dataCents, data):
    i = 0
    newCentroids ={}
    for c in centroids:
        newCentPos = -1
        sum = 0
        count = 0
        j=0
        for d in data:
            if(dataCents[j] == i):
                sum += d
                count+=1
            j+=1
        if(count > 0):
            newCentPos = sum/count
            newCentroids[i]=newCentPos
        else:
            newCentroids[i]=centroids[i]
        i +=1
    return newCentroids

def checkCentroids(new,old):
    count = len(new)
    for c in old:
        if(old[c] == new[c]):
            count -=1

    if(count == 0):
        return True
    else:
        return False
def main(input):
    
    #data = randData(1000)
    data = readData('auth_amt.csv')
    centroids = initCentroids(input,data)
    print('first centroids: ' + str(centroids))
    #print(data)
    # initing the first datapt:centroid index list
    dataCents = []
    for d in data:
        dataCents.append(nearestCentroid(centroids, d))

    centroids = refactorCentroids(centroids, dataCents, data)
    print(centroids)

    while(True):
        dataCents.clear()
        for d in data:
            dataCents.append(nearestCentroid(centroids, d))

        newCentroids = refactorCentroids(centroids, dataCents,data)
        if(checkCentroids(newCentroids,centroids)):
            break
        centroids = newCentroids
        print(centroids)

    print('\n\n')
    print('old dc: '+str(dataCents))
    #centroids = sortify(centroids, dataCents)
    print('final centroids: '+ str(centroids))
    print('data:           '+ str(data))
    print('data centroids: '+str(dataCents))
    ones = []
    #centroids = sorted(centroids.items(), key=operator.itemgetter(1))
    print(centroids)
    for i in range(len(centroids)):
        ones.append(1)
    mores = []
    for j in range(len(data)):
        mores.append(1)

    min(centroids.items(), key=lambda x: x[1])
    index = 0
    while(len(centroids)>0):
        minimum = min(centroids.items(),key=lambda x:x[1])
        centroids.pop(minimum[0])
        mat.scatter(minimum[1],3*index,s=30)
        dataList = []
        ptList = []
        i=0
        for d in dataCents:
            if(d == minimum[0]):
                dataList.append(data[i])
                ptList.append(3*index + np.random.uniform(-1,1))
            i+=1
        print('num in cluster '+ str(minimum[0])+' located at: '+str(minimum[1])+' ::::: '+str(len(dataList)))
        mat.scatter(dataList,ptList,s=4)
        index +=1
    mat.show()

if __name__ == '__main__':
    try:

        for ix in range(1,10):
            main(ix*2)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

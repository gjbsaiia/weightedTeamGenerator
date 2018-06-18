import numpy as np
import sys
import os
import matplotlib.pyplot as mat


def initCentroids(numCentroids):
    centroids = {}
    for i in range(numCentroids):
        centroids[i] = (int(np.random.rand(1)*100))
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
        data.append(int(np.random.rand(1)*100))
    return data

def dist(c,d):
    return abs(c-d)

def refactorCentroids(centroids,tuples):
    i = 0
    newCentroids ={}
    for c in centroids:
        newCentPos = -1
        sum = 0
        count = 0
        for d in tuples:
            if(tuples[d] == i):

                sum += d
                count+=1
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
def main():
    centroids = initCentroids(8)
    data = randData(100)
    print('first centroids: ' + str(centroids))
    #print(data)
    # initing the first datapt:centroid index list
    tuples = {} # this is list with key being [datapoint,centroid index]
    for d in data:
        tuples[d] = nearestCentroid(centroids,d)

    centroids = refactorCentroids(centroids, tuples)
    print(centroids)

    while(True):
        for d in data:
            tuples[d] = nearestCentroid(centroids, d)

        newCentroids = refactorCentroids(centroids, tuples)
        if(checkCentroids(newCentroids,centroids)):
            break
        centroids = newCentroids
        print(centroids)

    print('\n\n')
    print('final centroids: '+ str(centroids))
    print('data: '+ str(tuples))
    ones = []
    for i in range(len(centroids)):
        ones.append(1)
    mores = []
    for j in range(len(tuples)):
        mores.append(1)

    for pt in centroids:
        RGB = (np.random.rand(1),np.random.rand(1),np.random.rand(1))
        mat.scatter(centroids[pt],pt,s=10)
        dataList = []
        ptList = []
        for d in tuples:
            if(tuples[d] == pt):
                dataList.append(d)
                ptList.append(tuples[d])

        mat.scatter(dataList,ptList,s=2)
    mat.show()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
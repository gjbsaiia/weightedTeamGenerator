import os
import sys
import numpy as np

teamSize = 5

def getNoOfClusters(listing, teamSize):
    #totalPeople = len(listing)
    n = len(listing)/teamSize
    m = len(listing)/(teamSize*1.0)
    if((n*1.0) == (m*1.0)):
        return n
    else:
        return n + 1

def dist(new, centroid):
    return ((centroid - new) ** 2)

def allocateTeams(clusters, centers, listing):
    for each in listing:
        cut = each.split(' ')
        weight = int(cut[1])
        name = cut[0]
        min = 100
        nm = 0
        i = 0
        for center in centers:
            d = dist(weight, center)
            if (d < min):
                if len(clusters[i]) < teamSize:
                    min = d
                    nm = i
            i += 1
        clusters[nm].append(each)
        centers[nm] = recenter(centers[nm], clusters[nm])

def maxDeviation(clusters):
     maxDif = 1
     averages = []
     for cluster in clusters:
         averages.append(aveInCluster(cluster))
     for ave1 in averages:
         for ave2 in averages:
             if  ((ave1 - ave2) ** 2) > maxDif:
                 maxDif = ((ave1 - ave2) ** 2)
     return maxDif

def aveInCluster(cluster):
     total = 0
     print(cluster)
     for member in cluster:
         cut = member.split(' ')
         weight = int(cut[1])
         total += weight
     return ((total+0.0)/len(cluster))

def recenter(center, cluster):
    ave = 0
    i = 0
    while i < len(cluster):
        cut = cluster[i].split(' ')
        weight = int(cut[1])
        ave += weight
        i+=1
    return (ave+0.0)/len(cluster)

def cleanUpClusters(clusters):
    for cluster in clusters:
        team = []
        for entry in cluster:
            cut = entry.split(' ')
            name = cut[0]
            team.append(name)
        cluster = team

def initCentroids(numCentroids):
    centroids = []
    for i in range(numCentroids):
        centroids.append((int)(np.random.rand(1)*10))
    return centroids

def main():
    filename = "listing.txt"
    print("welcome to balanced tug o' war team generator")
    line = " "
    listing = []
    clusters = []
    centers = []
    line = input("file entry, or manual entry? ")
    flag = 0
    while 1:
        if(line == "manual"):
            flag = 1
            break
        if(line == "file"):
            flag = 0
            break
        input("type either 'file' or 'manual': ")
    if flag == 1:
        line = input("please enter a name and a weight, or done: ")
        while line != "done":
            listing.append(line)
            line = input("please enter a name and a weight, or done: ")
    else:
        with open(filename) as names:
            lines = names.readlines()
            names.close()
        for line in lines:
            split = line.split('\n')
            listing.append(split[0])
    i = 0
    n = getNoOfClusters(listing, teamSize)
    print('n: ' + str(n))
    while(i < n):
        clusters.append([])
        centers.append(0)
        i += 1
    allocateTeams(clusters, centers, listing)
    print('clusters post alloc: ')
    deviation = maxDeviation(clusters)
    print("First round:")
    print(clusters)
    print(deviation)
    while(deviation > 2):
        print('reach')
        print(clusters)
        allocateTeams(clusters, centers, listing)
        deviation = maxDeviation(clusters)
    cleanUpClusters(clusters)
    print(deviation)
    print(clusters)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

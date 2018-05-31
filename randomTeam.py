import os
import sys
import numpy as np

teamSize = 5

def getNoOfClusters(listing, teamSize):
	 totalPeople = len(listing)
	 n = len(listing)/teamSize
	 m = len(listing)/teamSize
	 if(n == m):
		 return n

 	 else:
		 if(teamSize == 5):
		 	teamSize = 6
		 	getNoOfClusters(listing,teamSize)
	 	 else:
		 	return n + 1

def dist(new, centroid):
	 return ((centroid - new) ** 2)

def allocateTeams(clusters, centers, listing):
	 for each in listing:
		cut = listing.split(' ')
		weight = cut[1]
		name = cut[0]
	 	min = 10
		nm = 0
		i = 0
	 	for center in centers:
			d = dist(weight, center)
		 	if (d < min & (len(cluster[i]) < teamSize)):
				min = d
				nm = i
			i += 1
		clusters[i].append(listing)
		centers[i] = recenter(centers[i], clusters[i])

def maxDeviation(clusters):
	 maxAve = 10
	 for cluster in clusters:
		 total = 0
		 for member in cluster:
			 cut = member.split(' ')
			 weight = cut[1]
			 total += weight
		 ave = (total+0.0) / len(cluster)
		 if(ave > maxAve):
			 maxAve = ave
	 return maxAve

def recenter(i, center, cluster):
	ave = 0
	for entry in cluster:
		cut = entry.split(' ')
		weight = cut[1]
		ave += weight
	return (ave+0.0)/len(cluster)

def cleanUpClusters(clusters):
	for cluster in cluster:
		team = []
		for entry in cluster:
			cut = entry.split(' ')
			name = cut[0]
			team.append(name)
		cluster = team

def main():
	print "welcome to 'random' tug o' war team generator"
 	line = " "
 	listing = []
 	clusters = []
 	while line != "done":
 		line = raw_input("please enter a name and a weight or done: ")
		listing.append(line)
	i = 0
	while(i < getNoOfClusters(listing, teamSize)):
		clusters.append([])
 	centers = np.zeros(getNoOfClusters(listing, teamSize))
	allocateTeams(clusters, centers, listing)
 	deviation = maxDeviation(clusters)
	while(deviation > 2):
		allocateTeams(clusters, centers, listing)
		deviation = maxDeviation(clusters)
	cleanUpClusters(clusters)
	print clusters

if __name__ == '__main__':
	try:
    	main()
	except KeyboardInterrupt:
    	print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

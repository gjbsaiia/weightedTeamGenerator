import os
import sys
import numpy as np

teamSize = 5

def getNoOfClusters(listing, teamSize):
	 totalPeople = len(listing)
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
		clusters[nm].append(listing)
		centers[nm] = recenter(centers[nm], clusters[nm])
		i = 0
		for cluster in clusters:
			print i
			print centers[i]
			for name in cluster:
				print name
			i += 1

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

def recenter(center, cluster):
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
	filename = "listing.txt"
	print "welcome to balanced tug o' war team generator"
	line = " "
	listing = []
	clusters = []
	line = raw_input("file entry, or manual entry? ")
	flag = 0
	while 1:
		if(line == "manual"):
			flag = 1
			break
		if(line == "file"):
			flag = 0
			break
		raw_input("type either 'file' or 'manual': ")
	if flag == 1:
		line = raw_input("please enter a name and a weight, or done: ")
		while line != "done":
			listing.append(line)
			line = raw_input("please enter a name and a weight, or done: ")
	else:
		with open(filename) as names:
			lines = names.readlines()
			names.close()
		for line in lines:
			split = line.split('\n')
			listing.append(split[0])
	i = 0
	print listing
	getNoOfClusters(listing, teamSize)
	while(i < teamSize):
		clusters.append([])
		i += 1
	print teamSize
	centers = np.zeros(getNoOfClusters(listing, teamSize))
	allocateTeams(clusters, centers, listing)
	deviation = maxDeviation(clusters)
	print clusters
	print deviation
	#while(deviation > 2):
	#	allocateTeams(clusters, centers, listing)
	#	deviation = maxDeviation(clusters)
	#cleanUpClusters(clusters)
	#print clusters

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

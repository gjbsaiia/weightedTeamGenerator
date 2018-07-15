# Tug 'O War Balanced Team Allocation
# Progressive Insurance, ETS Operations Intern Picnic
# Griffin Saiia

# Algorithm:
# 	- Determine no. of clusters ( poolSize / clusterSize )
#			--> Make list for each cluster
#			--> Each cluster is a tuple, (weight of cluster, cluster)
#	- Sort pool by weight, max->min
#	- Pool is tiered into rounds of picks. At the end of each round, each cluster
# 	  is evaluated. Lightest cluster gets first pick next round.
#			--> Evaluation is done by calculating the total weight of a team
#				and sorting them from min-->max.
#
# This is essentially a greedy algorithm with K-mean sensibilities.
#
# Variable Key:
# pool: List of tuples, [contestant, strength weighting]
# poolSize: No. of contestants
# poolWeightSum: Sum of all weights in pool
# cluster: A team!
# clusterSize: Ideal team size (5 in our case)
# targetClusterAve: Target weight for a given clusters
#					poolWeightSum / ( poolSize / cluster size )
#					This isn't used anywhere in the program, but is
#					a guide to measure how the algorithm holds up.
# tieredPool: The ordered pool segmented into rounds of picks
#			  (think an automated fantasy football draft)
# tier: One round of picks

import os
import sys

#target team size
clusterSize = 5

def main():
	pool = start()
	clusterList = setClusters(pool)
	sortTupleList(pool, True)
	tieredPool = tierPool(pool, clusterList)
	allocateClusters(tieredPool, clusterList)
	printClusters(clusterList)
	targetClusterAve = totalWeight(pool) / ( len(pool) / clusterSize)
	print("Target clusterweight: "+str(targetClusterAve))
	writeOutClusters(clusterList)

# the wrapper for the program
def start():
	print("--------------------------------------------------------")
	print("Welcome to the Progressive Tug O War Team Generator")
	print("        o  o  o                  o  o  o              ")
	print("        |-<|-<|--<~~~~~~~~~~~~>--|>-|>-|              ")
	print("        |\ |\ |\                /| /| /|              ")
	print("--------------------------------------------------------")
	line = ""
	pool = []
	line = raw_input("manual entry or file entry? ")
	while(1):
		if(line == "manual"):
			break
		if(line == "file"):
			break
		# calls a testing method I wrote that skips the prompts
		if(line == "test"):
			break
		print("not a recognized command.")
		print("manual entry or file entry?")
		line = raw_input("enter 'manual' or 'file': ")
	if(line == 'manual'):
		pool = manualEntry(pool)
	if(line == "file"):
		pool = fileEntry(pool)
	if(line == "test"):
		pool = test()
	return pool

# allows for manual contestant entry
def manualEntry(pool):
	print("enter contestants in the following format:")
	print("<Firstname,Lastname> <Weight>")
	print("enter 'oops' to remove last entry, and 'done' when finished")
	line = ""
	while(line != 'done'):
		if(line != ""):
			if(line == "oops"):
				pool = removeLast(pool)
			else:
				# formats the tuple for easy printing later
				split = line.split(" ")
				name = split[0].split(",")
				tuple = [name[0]+" "+name[1], int(split[1])]
				pool.append(tuple)
		line = raw_input("enter contestant: ")
	print("current pool:")
	printPool(pool)
	print("pool size: "+str(len(pool)))
	line = raw_input("do you need to add more contestants?(y/n) ")
	if(line == "y"):
		pool = manualEntry(pool)
	line = raw_input("would you like to add contestants from a .txt file? (y/n) ")
	if(line == "y"):
		pool = fileEntry(pool)
	return pool

# quick and dirty method to remove a unwanted entry
def removeLast(pool):
	newPool = []
	if(len(pool) > 1):
		i = 0
		while(i < (len(pool) - 1)):
			newPool.append(pool[i])
			i += 1
		return newPool
	else:
		return newPool

# allows for mass contestant entry through a .txt file
def fileEntry(pool):
	filename = ""
	lines = []
	while(1):
		filename = raw_input("enter local .txt filename: ")
		try:
			with open(filename) as names:
				lines = names.readlines()
				names.close()
			break
		except:
			print('File not found. :(')
	for line in lines:
		# formats the tuple for easy printing later
		entry = line.split("\n")
		split = entry[0].split(' ')
		name = split[0].split(",")
		tuple = [name[0]+" "+name[1], int(split[1])]
		pool.append(tuple)
	print("current pool:")
	printPool(pool)
	print("pool size: "+str(len(pool)))
	line = raw_input("would you like to use an additional file? (y/n): ")
	if(line == "y"):
		pool = fileEntry(pool)
	line = raw_input("any contestants to add manually? (y/n): ")
	if(line == "y"):
		pool = manualEntry(pool)
	return pool

# initializes clusterList
def setClusters(pool):
	numOfClusters = len(pool) / clusterSize
	clusterList = []
	i = 0
	while(i < numOfClusters):
		clusterList.append([0, []])
		i += 1
	return clusterList

# max/min ordering quicksort specific to a tuple list
# key: true, max ordering
# key: false, min ordering
def sortTupleList(tupleList, key):
	sortTupleListHelper(tupleList, 0, len(tupleList) - 1, key)
# still just quicksort
def sortTupleListHelper(tupleList, first, last, key):
	if(first < last):
	   split = tupleListPartition(tupleList, first, last, key)
	   sortTupleListHelper(tupleList, first, split - 1, key)
	   sortTupleListHelper(tupleList, split + 1, last, key)
# quicksort is so verbose but so so nice
def tupleListPartition(tupleList, first, last, key):
	pivot = tupleList[first]
	left = first + 1
	right = last
	done = False
	while(not done):
		# for sorting max->min
		if(key):
		   while(left <= right and tupleList[left][1] >= pivot[1]):
		       left = left + 1
		   while(right >= left and tupleList[right][1] <= pivot[1]):
		       right = right-1
	    # for sorting min->max
	   	else:
   		   while(left <= right and tupleList[left][1] <= pivot[1]):
   		       left = left + 1
   		   while(right >= left and tupleList[right][1] >= pivot[1]):
   		       right = right-1
		if(right < left):
		   done = True
		else:
		   hold = tupleList[left]
		   tupleList[left] = tupleList[right]
		   tupleList[right] = hold
	hold = tupleList[first]
	tupleList[first] = tupleList[right]
	tupleList[right] = hold
	return right

# method that tiers the presorted pool into rounds of picks
def tierPool(pool, clusterList):
	tieredPool = []
	numOfTiers = len(pool)/len(clusterList)
	checkNumOfTiers = (len(pool)+0.0) / (len(clusterList)+0.0)
	if( numOfTiers != checkNumOfTiers ):
		numOfTiers += 1
	i = 0
	while(i < numOfTiers):
		tieredPool.append([])
		i += 1
	i = 0
	j = 0
	# yeah I know double loops are gross
	# could've made this more efficient with a little more thinking in a
	# single loop, but this is a side project.
	for tier in tieredPool:
		j = 0
		while(j < len(clusterList) and i < len(pool)):
			tier.append(pool[i])
			i += 1
			j += 1
	return tieredPool

# distributes participants to each cluster according to the tiers of the List
# and the evaluative ordering
def allocateClusters(tieredPool, clusterList):
	# order that each cluster (referenced by index) gets to pick
	pickOrder = []
	# each tier is a round of picks
	for tier in tieredPool:
		i = 0
		for contestant in tier:
			# first round order is irrelevant
			if(pickOrder == []):
				clusterList[i][1].append(contestant)
			else:
				clusterList[pickOrder[i]][1].append(contestant)
			i += 1
		# pick order is set for next round
		pickOrder = evaluateClusters(clusterList, pickOrder)
	# this is only included for the organizer - shows how even the teams are
	# once the program finishes running
	for cluster in clusterList:
		cluster[0] = totalWeight(cluster[1])

# gets the total weight of each team, and sorts the weights - lightest
# cluster gets first pick next round
def evaluateClusters(clusterList, pickOrder):
	# zeros out the pickOrder
	pickOrder = []
	# weightsOfClusters is a list of tuples, [index of cluster, cluster weight]
	weightsOfClusters = []
	i = 0
	# calculating all the cluster's weights
	for cluster in clusterList:
		weightsOfClusters.append([i, totalWeight(cluster[1])])
		i += 1
	# sorts weightsOfCluster min->max
	sortTupleList(weightsOfClusters, False)
	# sets pick order by pulling the indexes of the clusters from
	# the sorted list of cluster weights
	for each in weightsOfClusters:
		pickOrder.append(each[0])
	return pickOrder

# lil helper that totals the weights of a pool or cluster
def totalWeight(tupleList):
	sum = 0
	i = 0
	while(i < len(tupleList)):
		sum += tupleList[i][1]
		i += 1
	return sum

# printing method
def printPool(pool):
	for tuple in pool:
		print("  - "+tuple[0]+", "+str(tuple[1]))
# printing methodddds
def printClusters(clusterList):
	print("Clusters:")
	i = 1
	for cluster in clusterList:
		print("Team "+str(i)+"'s Weight: "+str(cluster[0]))
		printPool(cluster[1])
		i += 1
# writes teams without any of the weighting to a .txt file for distribution
def writeOutClusters(clusterList):
	f = open("TugOWarTeams.txt", "w+")
	i = 1
	for cluster in clusterList:
		f.write("Team "+str(i)+": ")
		for tuple in cluster[1]:
			f.write(tuple[0]+"   ")
		f.write("\n")
		i += 1
	print("file written")

# lil test method that references an early sign up sheet
def test():
	pool = []
	filename = "TOW_7_2.txt"
	try:
		with open(filename) as names:
			lines = names.readlines()
			names.close()
	except FileNotFoundError:
		print('File not found. :(')
	for line in lines:
		entry = line.split("\n")
		split = entry[0].split(' ')
		name = split[0].split(",")
		tuple = [name[0]+" "+name[1], int(split[1])]
		pool.append(tuple)
	print("check over your current pool of "+str(len(pool))+" people:")
	printPool(pool)
	return pool

# to run it from command line
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("")
		print('Interrupted')
        try:
			sys.exit(0)
	except SystemExit:
			os._exit(0)

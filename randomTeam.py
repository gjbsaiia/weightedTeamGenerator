import os
import sys

 teamSize = 5

 def getTarget(weights):
	 totalWeight = 0
	 for each weight in weights:
		 totalWeight += weight
	 return ( totalWeight / len(weights) )

 def countingSort(weights, names, exp):
    n = len(weights)
    wOut = [0] * (n)
	nOut = []
    count = [0] * (10)
    for i in range(0, n):
        index = ( weights[i] / exp )
        count[ ( index )%10 ] += 1
    for i in range(1,10):
        count[i] += count[ i - 1 ]
    i = n - 1
    while i >= 0:
        index = ( weights[i] / exp )
        wOut[ count[ ( index )%10 ] - 1 ] = weights[i]
		nOut[ count[ ( index )%10 ] - 1 ] = names[i]
        count[ ( index )%10 ] -= 1
        i -= 1
    i = 0
    for i in range(0, len(weights)):
        weight[i] = wOut[i]
		names[i] = nOut[i]

 def radixSort(weights, names):
    maximum = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(weights, names, exp)
        exp *= 10



 def main():
	 print "welcome to 'random' tug o' war team generator"
	 line = " "
	 listing = []
	 names = []
	 weights = []
	 teams = []
	 while line != "done":
	 	line = raw_input("please enter a name and a weight or done: ")
		listing.append(line)
		split = line.split(' ')
		names.append(split[0])
		weights.append(split[1])
	targetWeight = getTarget(weights)
	noOfTeams = (len(names) / teamSize)
	radixSort(weights)
	allocateTeams(teams, weights, names)






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

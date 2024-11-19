'''
# Q1. Airpot Baggage

The airport baggage department needs to distribute N bags on K storage slots. Initially 
all slots are empty. The bags are distributed in a cyclical pattern, starting with one 
bag in the first slot, and so on until the kth slot is filled with K bags. The cycle then 
repeats, with K+1 bags in the first slot, K+2 bags in the second slot, and so on. This 
process continues untill all N bags are distributed. The output should be an array 
containing the total number of bags in each storage slot.

Examples:
Input:
N = 10
K = 5

Output:
1 2 3 4 0
'''


def distributeBags(N, K):
	result = [0] * K # initialize a list of K elements with zero bags
	indx = 0
	while N > 0: # loop until we have no more bags to distribute
		bag_to_store = min(N, indx+1)
		result[indx % K] += bag_to_store # distribute bags to the i-th slot
		N -= bag_to_store # subtract the distributed bags from N
		indx += 1 # move to the next slots
	return result

if __name__ == '__main__':
	N = 10
	K = 5
	result = distributeBags(N, K)
	for i in range(K):
		print(result[i], end=" ")
	

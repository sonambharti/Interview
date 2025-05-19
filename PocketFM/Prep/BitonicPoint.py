"""
Write a program to find bitonic point in a bitonic array. 

A Bitonic Sequence is a sequence of numbers that is first strictly increasing then after a point decreasing.
"""
# Function to find bitonic point using binary search 
def recursive_binarySearch(arr, left, right): 

	if (left <= right): 

		mid = (left + right) // 2; 

		# base condition to check if arr[mid] is bitonic point or not
		if (arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]): 
			return mid; 

		if (arr[mid] < arr[mid + 1]): 
			return binarySearch(arr, mid + 1,right); 
		else: 
			return binarySearch(arr, left, mid - 1); 

	return -1; 

def iterative_binarySearch(arr, low, high): 
      
    # binary search iterativ 
    while(low <= high): 
        
        # finding the mid index 
        mid = low + (high - low) // 2
          
        # if both the values on either side 
        # of mid index is lesser 
        if(arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]): 
            return mid 
        # move to the right part 
        elif(arr[mid] < arr[mid + 1]): 
            low = mid + 1
              
        # move to the right part 
        else: 
            high = mid - 1
    # Not Found 
    return -1
    
if __name__ == "__main__":
    arr = [6, 7, 8, 11, 9, 5, 2, 1]; 
    n = len(arr); 
    index = recursive_binarySearch(arr, 1, n-2); 
    if (index != -1): 
    		print(arr[index]); 
    
    index = iterative_binarySearch(arr, 1, n-2); 
    if (index != -1): 
    		print(arr[index]); 

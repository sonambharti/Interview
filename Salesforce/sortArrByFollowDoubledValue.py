#sort Array By Follow Doubled Value

"""
An integer array original is transformed into a doubled array sortArray 
by appending twice the value of every element in original, and then 
return an array which contains each element at even indexes should be 
followed by double value at odd indexes.
Given an array sortArray, return original if sortArray is a doubled array. 
Otherwise return [].
"""

def sortArrByFollowDoubledValue(sortArray):
    n = len(sortArray)
    outputArray = []
    
    if(n%2 != 0):
        return []
        
    flag = True
    for i in range(0, n-1, 2):
        if(sortArray[i+1] != 2*sortArray[i]):
            flag = False
    
    if flag == True:
        # print("Flag = ", flag)
        return sortArray
        
    sortArray.sort()
    
    el = sortArray[0]
    outputArray.append(el)
    sortArray.remove(el)
    
    
    for i in range(n-2):
        el2 = 2*el
        if(el2 in sortArray):
            outputArray.append(el2)
            sortArray.remove(el2)
        else:
            return []
            
        if(len(sortArray) != 0):
            el = sortArray[0]
            outputArray.append(el)
            sortArray.remove(el)
    
    return outputArray
    
    
if __name__ == "__main__":
    n = int(input("Enter size of list: "))
    sortArray = []
    print("Enter values of array: ")
    for i in range(n):
        el = int(input())
        sortArray.append(el)
        
    res = sortArrByFollowDoubledValue(sortArray)
    print("Output: ", res)

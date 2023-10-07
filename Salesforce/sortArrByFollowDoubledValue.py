# String Palindrome

"""
Description: Given a  String s, return integer for count 
of all the unique palindromic, permutations of it. 
If s has no palindromic permutation, return 0.

s consists of only lowercase English letters.
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
        if(el2 not in sortArray):
            return []
        else:
            outputArray.append(el2)
            print(outputArray)
            sortArray.remove(el2)
            
        if(len(sortArray) != 0):
            el = sortArray[0]
            outputArray.append(el)
            sortArray.remove(el)
        else:
            break
    
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

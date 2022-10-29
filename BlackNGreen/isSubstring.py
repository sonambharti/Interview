def isSubstring(str1, str2):
    m = len(str1)
    n = len(str2)
    
    for i in range(m-n+1):
        for j in range(n):
            if(str1[i+j] != str2[j]):
                break
        if j+1 == m:
            return i
    return -1

str1 = "Interview"
str2 = "viewInter"

res = isSubstring(str1, str2)

if res == -1:
    print("not present")
    
else:
    print("present")

"""
if str2 in str1:
    print("present")
else:
    print("not present")
    
"""

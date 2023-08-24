"""
You're provided with two arrays:

"geeksTown" of length n - representing the heights of buildings in Geek's town
"journey" of length m      - representing the heights of buildings he sees during his train journey.
Geek finds happiness when he encounters a series of buildings during his journey that completely match with geeksTown.

You have 'q' queries of the form [l, r], where you need to determine how many times Geek will feel happy during the journey  from [l, r].

Example:

Input:
n = 4,
geeksTown[] = {3, 0, 1, 9},
m = 11,
journey[] = {1, 3, 0, 1, 9, 1, 7, 3, 0, 1, 9},
q = 4,
queries[] = [
 [0, 3],
 [1, 5],
 [1, 10],
 [7, 9]
]
Output:
0 1 2 0

"""

def z_func(a, n):
    z = [0 for i in range (n)]
    l=0
    r=0
    
    for i in range(1, n):
        if i<r:
            z[i] = min(r-i, z[i-l])
        while ((i + z[i] < n) and (a[z[i]] == a[i+z[i]])):
            z[i] += 1
        if (i + z[i] > r):
            l = i
            r = i + z[i]
            
    return z
    
    
def combine(a, n, b, m):
    ans = [0 for i in range(n + m + 1)]
    
    for i in range(0, n):
        ans[i] = a[i]
        
    ans[n] = -1
    
    for i in range(0, m):
        ans[i + n + 1] = b[i]
        
    return ans
    
    
def geeksJourney(geeksTown, n, journey, m, queries, q):
    # code here
    
    a = combine(geeksTown, n, journey, m)
    z = z_func(a, len(a))
    
    Pref = [0 for i in range(m)]
    
    for i in range(n+1, len(z)):
        if z[i] == n:
            Pref[i - n - 1] = 1
            
    for i in range(1, m):
        Pref[i] += Pref[i-1]
        
    ans = [0 for i in range(q)]
    
    for i in range(0, q):
        l = queries[i][0]
        r = queries[i][1] - n + 1
        
        if l > r:
            ans[i] = 0
            continue
        
        ans[i] = Pref[r] - (0 if l == 0 else Pref[l-1])
        
    return ans
    
if __name__ == '__main__':
    geeksTown = [3, 0, 1, 9]
    n = len(geeksTown)
    
    Journey = [1, 3, 0, 1, 9, 1, 7, 3, 0, 1, 9]
    m = len(Journey)
    
    queries = [[0, 3],[1, 5],[1, 10],[7, 9]]
    q = len(queries)
    
    res = geeksJourney(geeksTown, n, Journey, m, queries, q)
    print(res)

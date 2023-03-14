"""
code to find min platform required to hault the trains....
"""

# Naive approach

def findMinmPlatform(arrival_list, departure_list):
    min_plat = 1
    count = 1

    for i in range(len(arrival_list)):
        count = 1 
        for j in range(len(departure_list)):
            if i != j:
                if(arrival_list[i] >= arrival_list[j] and deparature_list[j] >= arrival_list[i]):
                    count += 1
        min_plat = max(min_plat, count)

    return min_plat

# Optimized Approach

def OptimalfindMinmPlatform(arrival_list, departure_list):
    
    count = 1
    min_plat = 1
    arrival_list.sort()
    departure_list.sort()

    n = len(arrival_list)


    i = 1
    j = 0
    while(i<n and j<n):
        if(arrival_list[i] <= departure_list[j]):
            count += 1
            i += 1
        elif(arrival_list[i] > departure_list[j]):
            count -= 1
            j += 1

        if min_plat < count:
            min_plat = count
    return min_plat

if __name__ == "__main__":
    arrival_list = [900, 940, 950, 1100, 1500, 1800]
    deparature_list = [910, 1200, 1120, 1130, 1900, 2000]

    res_naive = findMinmPlatform(arrival_list, deparature_list)
    print("Naive Approach Sol: ",res_naive)

    res_optimal = findMinmPlatform(arrival_list, deparature_list)
    print("Optimal Approach Sol: ",res_optimal)

    

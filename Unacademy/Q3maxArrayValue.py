'''
# Q3. Maximum value by rearrangement

You are given an Array containing N elements. You are allowed to rearrange the elements 
of the array. The value of the array is defined as (A[0])*(A[0] | A[1])*A[0] | A[1] | 
A[2])*.....*(A[0] | A[1] | A[2] | A[3] | ... | A[N-1]), where '|' denotes the bitwise 
OR operator. You are taskedwith finding the maximum value of the array after the
rearrangement. Since the answer could be large, please print it modulo 1e9+7.

Examples:
Input:
N = 5
A = [1, 2, 3, 4, 5]
Output:
12005

'''


def maxArrayValue(N, A):
    def sort_bit(A):
        res = []
        current_or = 0
        while A:
            max_or = -1
            best_num = -1
            best_index = -1
            for i in range(len(A)):
                potential_or = current_or | A[i]
                if potential_or > max_or:
                    max_or = potential_or
                    best_num = A[i]
                    best_index = i
            res.append(best_num)
            current_or = max_or
            A.pop(best_index)
        return res
    
    MOD = 10**9 + 7

    A = sort_bit(A)

    # A.sort(key=lambda x: (-bin(x).count('1'), -x))

    cur = 0
    res = 1
    
    for num in A:
        cur |= num 
        res = (res * cur) % MOD 
    
    return res


if __name__ == "__main__":
    N = 5
    A = [1, 2, 3, 4, 5]
    print(maxArrayValue(N, A))  # Output: 12005

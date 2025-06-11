'''
# Maximum Profit from Sequential Subsequence Bouquets
You are given a binary string s, where each character represents a flower:

'0' → rose

'1' → lily

You can form two types of bouquets by picking flowers in index order (i.e. as a subsequence), not necessarily
adjacent:

Type P: pick three roses ("000") → earns profit p

Type Q: pick one rose then one lily ("01") → earns profit q

Rules
You choose bouquets one at a time, removing the picked flowers from further consideration.

For each bouquet:
Type P: select any three remaining '0's in increasing index order.
Type Q: select any '0' and a later '1' in increasing index order.

No flower can be used in more than one bouquet.

You may pick bouquets in any order to maximize total profit.

Return the maximum profit you can achieve.

Examples
Example 1

s = "01010"
p = 5
q = 2
# You can pick three roses at indices 0,2,4 → one Type P bouquet → profit = 5
# Alternatively, you could form two Type Q bouquets ("01" twice) → profit = 4
# Best is profit = 5.
Output: 5

Example 2

s = "00001"
p = 5
q = 2
# Strategy:
#  - Pick three roses at indices [0,1,2] → +5
#  - Then pick rose at 3 and lily at 4 for "01" → +2
# Total = 7
Output: 7
'''

from typing import List
# Greedy Simulation - doesn't guarantee optimal solution
def maxProfit_greedy(s: str, p: int, q: int) -> int:
    from collections import deque

    zero_indices = deque([i for i, ch in enumerate(s) if ch == '0'])
    one_indices = deque([i for i, ch in enumerate(s) if ch == '1'])
    
    profit = 0

    def make_type_q():
        nonlocal profit
        used_zeros = []
        used_ones = []
        while zero_indices and one_indices:
            if zero_indices[0] < one_indices[0]:
                used_zeros.append(zero_indices.popleft())
                used_ones.append(one_indices.popleft())
                profit += q
            else:
                one_indices.popleft()
        return used_zeros, used_ones

    def make_type_p():
        nonlocal profit
        used = []
        while len(zero_indices) >= 3:
            used.extend([zero_indices.popleft() for _ in range(3)])
            profit += p
        return used

    # Prefer the more profitable bouquet
    if p > 3 * q:
        make_type_p()
        make_type_q()
    else:
        used_q0, used_q1 = make_type_q()
        make_type_p()

    return profit



# Startegy + Pick max -> may fail -> O(n)
from collections import deque

def maxProfit(s: str, p: int, q: int) -> int:
    def simulate(order):
        zeros = deque([i for i, ch in enumerate(s) if ch == '0'])
        ones = deque([i for i, ch in enumerate(s) if ch == '1'])
        used = set()
        profit = 0

        if order == 'P_first':
            # Try forming Type P bouquets first
            while len(zeros) >= 3:
                a, b, c = zeros.popleft(), zeros.popleft(), zeros.popleft()
                used.update([a, b, c])
                profit += p
            # Now try Type Q from remaining flowers
            zeros = deque([i for i in zeros if i not in used])
            ones = deque([i for i in ones if i not in used])
            while zeros and ones:
                if zeros[0] < ones[0]:
                    used.update([zeros.popleft(), ones.popleft()])
                    profit += q
                else:
                    ones.popleft()

        elif order == 'Q_first':
            while zeros and ones:
                if zeros[0] < ones[0]:
                    used.update([zeros.popleft(), ones.popleft()])
                    profit += q
                else:
                    ones.popleft()
            # Now try Type P
            zeros = deque([i for i in zeros if i not in used])
            while len(zeros) >= 3:
                a, b, c = zeros.popleft(), zeros.popleft(), zeros.popleft()
                used.update([a, b, c])
                profit += p

        return profit

    return max(simulate('P_first'), simulate('Q_first'))
    
    
# dp approach -> maximize profit with accuracy -> O(n^2)
from functools import lru_cache

def maxProfitDP(s: str, p: int, q: int) -> int:
    n = len(s)

    @lru_cache(maxsize=None)
    def dp(i):
        if i >= n:
            return 0

        max_profit = dp(i + 1)  # Skip current char

        # Try forming Type P: find 3 '0's
        if s[i] == '0':
            count = 1
            j = i + 1
            while j < n and count < 3:
                if s[j] == '0':
                    count += 1
                j += 1
            if count == 3:
                max_profit = max(max_profit, p + dp(j))

            # Try forming Type Q: '0' then a later '1'
            j = i + 1
            while j < n and s[j] != '1':
                j += 1
            if j < n:
                max_profit = max(max_profit, q + dp(j + 1))

        return max_profit

    return dp(0)


if __name__ == "__main__":
    s = "0000011"
    p = 5
    q = 2
    print("Greedy approach: ", maxProfit_greedy(s, p, q))
    print("Startegy + Pick Maximum: ", maxProfit(s, p, q))
    print("DP approach: ", maxProfitDP(s,p,q))
    
    
    

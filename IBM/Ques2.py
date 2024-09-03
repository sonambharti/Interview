"""
Process scheduling algorithms are used by a CPU to optimally schedule the running processes.
A core can execute one process at a time, but a CPU may have multiple cores.

There are n processes where i_th process starts its execution at start[i] and end[i], both
inclusive. Find the minimum number of cores required to execute processes.

Example:
Input: n = 3, start = [1, 3, 4], end = [3, 5, 6]
Output: 2
"""

def getMinCores(start, end):
    events = []
    
    # Create events for start (+1) and end (-1)
    for i in range(len(start)):
        events.append((start[i], 1))    # process starts
        events.append((end[i] + 1, -1)) # process ends
    
    # Sort events: first by time, and then by type (-1 before +1 if they are equal)
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_cores = 0
    current_cores = 0
    
    # Sweep through the events
    for event in events:
        current_cores += event[1]
        max_cores = max(max_cores, current_cores)
    
    return max_cores
    
    
# Example usage:
if __name__ == "__main__":
    n = 3
    start = [1, 3, 4]
    end = [3, 5, 6]
    print(getMinCores(start, end))  # Output: 2

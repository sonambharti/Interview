'''
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in 
any order, but there's a constraint: there has to be a gap of at least n intervals between 
two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks. 
'''

from collections import Counter, deque
import heapq

def leastInterval_bruteforce(tasks, n):
    # Count frequency of tasks
    task_count = Counter(tasks)
    
    # Cooldown queue: (task, remaining_count, available_time)
    cooldown = deque()
    
    time = 0
    
    while task_count or cooldown:
        time += 1
        
        # Step 1: Release tasks from cooldown
        if cooldown and cooldown[0][2] == time:
            task, remaining, _ = cooldown.popleft()
            task_count[task] = remaining
        
        # Step 2: Execute a task if available
        if task_count:
            # Pick task with highest frequency
            current_task = max(task_count, key=task_count.get)
            remaining = task_count[current_task]
            
            # Remove it from active tasks
            del task_count[current_task]
            
            # Execute it (reduce count)
            remaining -= 1
            
            # If still remaining, push to cooldown
            if remaining > 0:
                cooldown.append((current_task, remaining, time + n + 1))
        # else: CPU idle
    
    return time


def leastInterval_heap(tasks, n):
    # Step 1: Count frequency of tasks
    task_count = Counter(tasks)
    
    # Step 2: Create a max heap (use negative values because Python has min-heap)
    max_heap = [-cnt for cnt in task_count.values()]
    heapq.heapify(max_heap)
    
    # Queue for cooldown: (remaining_count, available_time)
    cooldown = deque()
    
    time = 0  # Total intervals
    
    while max_heap or cooldown:
        time += 1
        
        # Step 3: If heap has tasks, execute the most frequent one
        if max_heap:
            count = heapq.heappop(max_heap)
            count += 1  # Reduce count (since negative)
            
            # If task still has remaining count, add to cooldown
            if count != 0:
                cooldown.append((count, time + n))
        
        # Step 4: If cooldown task is ready, push back to heap
        if cooldown and cooldown[0][1] == time:
            heapq.heappush(max_heap, cooldown.popleft()[0])
    
    return time


def leastInterval_optimized(tasks, n):
    # Count frequency of tasks
    task_count = Counter(tasks)
    
    # Find maximum frequency
    max_freq = max(task_count.values())
    
    # Count how many tasks have max frequency
    max_count = list(task_count.values()).count(max_freq)
    
    # Calculate minimum intervals using formula
    intervals = (max_freq - 1) * (n + 1) + max_count
    
    # Return the maximum of total tasks or calculated intervals
    return max(len(tasks), intervals)



if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    
    # tasks = ["A","C","A","B","D","B"] 
    # n = 1
    
    # tasks = ["A","A","A", "B","B","B"]
    # n = 3
    
    print("Brute Force Output:", leastInterval_bruteforce(tasks, n))
    print("Heap Approach Output:", leastInterval_heap(tasks, n))
    print("Optimized Output:", leastInterval_optimized(tasks, n))

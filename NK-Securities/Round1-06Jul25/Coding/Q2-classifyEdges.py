"""
# Q1.
A ride hailing company sometimes travels between cities. To avoid delays, a driver first 
checks for the shortest routes. There is a map of the cities and their bidirectional roads
represented by a graph of nodes and eciges. Determine the paths from the first node to the
last nocle and choose the shortest length. Now select all peths that are that length. These 
are the shortest paths. Return an array of strings. one for each road in order, where the 
value is YES if the road is along any shortest path or No if it is not. The roacis or edges
are nemed using their 1-besed Index within the Input arrays.


Example

given a map of g_nodes 6 nodes. the starting nodes. ending nodes and road lengths are:

Road        from/to/weight

1               (1, 2, 1)
2               (2, 3, 1)
3               (3, 4, 1)
4               (4, 5, 1)
5               (5, 1, 3)
6               (1, 3, 2)
7               (5, 3, 1)

-   The treveller must travel from sty I to ty rodes, so from node I to nodes cass
-   The shortest path is units long and there are three path of the length 1->5, 1->2->3->5, 1->3->5.
-   Return an array of strings for each in order where the value is YES if a road is along a shortest path 
    or NO if it is not. In this case, the resulting array is [YES, NO NO YES YES YES]. The third and fourth 
    roads connect nodes (3.4) and 4. respectively. They ans not on a shortest path one with a length of 3 in
    this case.
    
Sample Input 0:

g_nodes = 4, g_edges = 5
g_from = [1,2,1,3, 1]
g_to = [2,4,3,4,4]
g_weight = [1,1,1,2,2]

Sample Output:
YES
YES
NO
NO
YES

"""
def classifyEdges(g_nodes, g_from, g_to, g_weight):

    import heapq
    
    n = g_nodes
    m = len(g_from)
    # Build adjacency list for the undirected weighted graph
    adjacency = [[] for _ in range(n + 1)]
    for i in range(m):
        u = g_from[i]
        v = g_to[i]
        w = g_weight[i]
        adjacency[u].append((v, w))
        adjacency[v].append((u, w))
    
    # Use Dijkstra's algorithm to compute shortest distances from node 1 (source)
    INF = float('inf')
    dist_from_1 = [INF] * (n + 1)
    dist_from_1[1] = 0
    pq = [(0, 1)]  # priority queue of (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist_from_1[u]:
            # Skip if this is not the current shortest distance for u
            continue
        for v, w in adjacency[u]:
            new_dist = d + w
            if new_dist < dist_from_1[v]:
                dist_from_1[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    # Use Dijkstra's algorithm to compute shortest distances from node n (destination)
    dist_from_n = [INF] * (n + 1)
    dist_from_n[n] = 0
    pq = [(0, n)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist_from_n[u]:
            continue
        for v, w in adjacency[u]:
            new_dist = d + w
            if new_dist < dist_from_n[v]:
                dist_from_n[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    # Determine which edges lie on at least one shortest path from 1 to n
    shortest_distance = dist_from_1[n]
    result = []
    if shortest_distance == INF:
        # If no path from 1 to n exists, no edge can be on a shortest path
        result = ["NO"] * m
    else:
        for i in range(m):
            u = g_from[i]
            v = g_to[i]
            w = g_weight[i]
            # For edge (u, v) to be on some shortest path from 1 to n, one of the following must hold:
            # dist_from_1[u] + w + dist_from_n[v] == dist_from_1[n]  (path: 1 -> ... -> u -> v -> ... -> n)
            # or dist_from_1[v] + w + dist_from_n[u] == dist_from_1[n]  (path: 1 -> ... -> v -> u -> ... -> n)
            if dist_from_1[v] + w + dist_from_n[u] == shortest_distance or dist_from_1[u] + w + dist_from_n[v] == shortest_distance:
                result.append("YES")
            else:
                result.append("NO")
    return result
    
if __name__ == "__main__":
    g_nodes = 4
    g_edges = 5
    g_from = [1,2,1,3, 1]
    g_to = [2,4,3,4,4]
    g_weight = [1,1,1,2,2]
    
    res = classifyEdges(g_nodes, g_from, g_to, g_weight)
    print(res)

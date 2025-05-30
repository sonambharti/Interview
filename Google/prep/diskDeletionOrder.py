'''

✅ Problem Summary

You're managing:

Disks: These may be created from:
Nothing (root)
A snapshot of another disk.
Snapshots: Taken from a disk, and can be used to create new disks.
A snapshot can only be deleted when:
All disks created from it (and any disks created from those disks’ snapshots, recursively) are deleted first.

🔧 Goal:
Given a list of disks and snapshots, return a valid sequence to delete all disks, such that:

You never violate snapshot dependency constraints (i.e., no disk should exist if its parent snapshot is deleted).

'''
"""
#   🧪 Brute Force Approach -> (O(n^2))
    
✅ Idea:
    -   At each step, find a disk whose deletion won't violate any dependencies (i.e., no child disks depend on it).
    -   Repeatedly remove such "safe" disks.
📌 Steps:
    1.   Build a graph:
        -   Each disk points to its parent snapshot.
        -   Each snapshot points to the disks created from it.
    2.   Repeatedly:
        -   Find a disk with no children (leaf).
        -   Delete it.
        -   Update the graph.
🧱 Downsides:
    -   This could require repeatedly scanning the entire graph to find leaves ⇒ inefficient.
"""
def brute_force_disk_deletion(disks, snapshots):
    # Build a mapping from snapshot to list of disks created from it
    snapshots_to_disks = {}
    for disk in disks:
        snap = disk.get('created_from_snapshot')
        if snap:
            if snap not in snapshots_to_disks:
                snapshots_to_disks[snap] = []
            snapshots_to_disks[snap].append(disk['name'])
    
    # Build a reverse dependency graph: disk -> list of disks that depend on it
    dependencies = {disk['name']: set() for disk in disks}
    for snapshot in snapshots:
        snap_name = snapshot['name']
        parent_disk = snapshot['disk']
        #   Disk created from this snapshot depend on the parent Disk
        for disk in snapshots_to_disks.get(snap_name,[]):
            dependencies[disk].add(parent_disk)
    
    deletion_order = []
    
    while dependencies:
        #   Find a disk with no dependencies (no one depends on it)
        removable_disk = None
        for disk, deps in dependencies.items():
            if not deps:
                removable_disk = disk 
                break
        if not removable_disk:
            raise Exception("Cycle detected or invalid dependency - cannot resolve deletion order")
            
        #   Add it to the result
        deletion_order.append(removable_disk)
        
        #   Remove it from other disk's dependency lists
        for disk in dependencies:
            dependencies[disk].discard(removable_disk)
        
        #   Finally, remove it from the map 
        del dependencies[removable_disk]
        
    return deletion_order

    


"""
#   ⚡ Optimal Approach — Topological Sort (Kahn’s Algorithm)

This is clearly a DAG of dependencies.

✅ Idea:
-   Perform a topological sort of the disk dependency graph.
-   Disks that are not used by any other disk can be deleted first.

📌 Steps:
    1. Build a reverse dependency graph:
       - For each disk, track who depends on it.
    2. Count in-degrees (i.e., number of children or dependents).
    3. Initialize a queue with disks having zero in-degree.
    4. Repeatedly:
       - Remove a disk with 0 in-degree.
       - Reduce in-degree of its parent snapshot.
       - If the parent snapshot has no remaining dependent disks, it’s deletable.
    5. Add parent disk (if now deletable) to queue.

⏱ Time Complexity:
-   O(n + e): Where n is number of disks and e is number of edges (dependencies)
-   Space: O(n + e) for graph representation
"""

from collections import defaultdict, deque

def optimal_disk_deletion(disks, snapshots):
    # Build a graph of disk dependencies (child -> parent)
    graph = defaultdict(set)  # disk -> set of disks it depends on
    in_degree = defaultdict(int)  # disk -> number of disks depending on it

    # Build snapshot → disk map (disks created from snapshots)
    snapshot_to_disks = defaultdict(list)
    for disk in disks:
        snap = disk.get('created_from_snapshot')
        if snap:
            snapshot_to_disks[snap].append(disk['name'])

    # Build dependency graph from snapshots
    for snap in snapshots:
        snap_name = snap['name']
        parent_disk = snap['disk']
        for child_disk in snapshot_to_disks[snap_name]:
            graph[parent_disk].add(child_disk)  # parent_disk must be deleted after child_disk
            in_degree[child_disk] += 1

    # Add all disks with 0 in-degree (no dependencies) to the queue
    all_disks = set(d['name'] for d in disks)
    queue = deque()
    for disk in all_disks:
        if in_degree[disk] == 0:
            queue.append(disk)

    deletion_order = []

    while queue:
        disk = queue.popleft()
        deletion_order.append(disk)

        # For all disks that this disk was a dependency of:
        for dependent in graph[disk]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)

    if len(deletion_order) != len(all_disks):
        raise Exception("Cycle or unresolved dependency found")

    return deletion_order


if __name__ == "__main__":
    disks = [
            {'name': 'diskA'},
            {'name': 'diskB', 'created_from_snapshot': 'snapA'},
            {'name': 'diskC', 'created_from_snapshot': 'snapB'}
        ]
    
    snapshots = [
            {'name': 'snapA', 'disk': 'diskA'},
            {'name': 'snapB', 'disk': 'diskB'}
        ]
    
    print("Brute Force Deletion Order: ", brute_force_disk_deletion(disks, snapshots))
    
    print("Optimal Approach to find Deletion Order: ", optimal_disk_deletion(disks, snapshots))

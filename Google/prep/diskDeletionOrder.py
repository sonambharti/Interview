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

from collections import defaultdict, deque
def brute_force_disk_deletion(disks, snapshots):
    # Map snapshot name → parent disk
    snapshot_to_disk = {snap['name']: snap['disk'] for snap in snapshots}

    # Build reverse dependency: parent disk → set of children disks
    reverse_graph = defaultdict(set)
    all_disks = set()

    for disk in disks:
        disk_name = disk['name']
        all_disks.add(disk_name)
        snap_name = disk.get('created_from_snapshot')
        if snap_name and snap_name in snapshot_to_disk:
            parent_disk = snapshot_to_disk[snap_name]
            reverse_graph[parent_disk].add(disk_name)

    result = []
    deleted = set()

    while len(deleted) < len(all_disks):
        deleted_this_round = False

        for disk in all_disks:
            if disk in deleted:
                continue

            # ✅ Only delete disk if all its children have been deleted
            if all(child in deleted for child in reverse_graph[disk]):
                result.append(disk)
                deleted.add(disk)
                deleted_this_round = True
                break  # restart loop

        if not deleted_this_round:
            raise Exception("Cycle or unsatisfied dependency detected")

    return result
    
    


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
    graph = defaultdict(set)  # disk -> set of disks it depends on (must be deleted after them)
    in_degree = defaultdict(int)  # disk -> number of disks it depends on

    snapshot_to_disks = defaultdict(list)
    for disk in disks:
        snap = disk.get('created_from_snapshot')
        if snap:
            snapshot_to_disks[snap].append(disk['name'])

    for snap in snapshots:
        snap_name = snap['name']
        parent_disk = snap['disk']
        for child_disk in snapshot_to_disks.get(snap_name, []):
            # ✅ CORRECT: To delete parent, all children must be deleted first
            graph[child_disk].add(parent_disk)
            in_degree[parent_disk] += 1

    all_disks = set(d['name'] for d in disks)
    queue = deque()

    # Disks with no dependencies can be safely deleted first
    for disk in all_disks:
        if in_degree[disk] == 0:
            queue.append(disk)

    deletion_order = []

    while queue:
        disk = queue.popleft()
        deletion_order.append(disk)

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
            {'name': 'snapB', 'disk': 'diskB'},
            {'name': 'snapC', 'disk': 'diskC'},
        ]
    
    print("Brute Force Deletion Order: ", brute_force_disk_deletion(disks, snapshots))
    
    print("Optimal Approach to find Deletion Order: ", optimal_disk_deletion(disks, snapshots))

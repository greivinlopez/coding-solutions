# -----------------------
# 743. Network Delay Time
# -----------------------

# Problem: https://leetcode.com/problems/network-delay-time/
# 
# You are given a network of n nodes, labeled from 1 to n. You are also given 
# times, a list of travel times as directed edges times[i] = (ui, vi, wi), 
# where ui is the source node, vi is the target node, and wi is the time it 
# takes for a signal to travel from source to target.
# 
# We will send a signal from a given node k. Return the minimum time it takes 
# for all the n nodes to receive the signal. If it is impossible for all the n 
# nodes to receive the signal, return -1.
# 
#  
# Example 1:
# 
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# 
# 
# Example 2:
# 
# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# 
# 
# Example 3:
# 
# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1 
# 
# 
# Constraints:
# 
#   1 <= k <= n <= 100
#   1 <= times.length <= 6000
#   times[i].length == 3
#   1 <= ui, vi <= n
#   ui != vi
#   0 <= wi <= 100
#   All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

import heapq
import collections

# Solution: https://youtu.be/EaphyqKU4PQ
# Credit: Navdeep Singh founder of NeetCode
def network_delay_time(times, n, k):
    edges = collections.defaultdict(list)
    for u, v, w in times:
        edges[u].append((v, w))

    minHeap = [(0, k)]
    visit = set()
    t = 0
    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = w1

        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minHeap, (w1 + w2, n2))
    return t if len(visit) == n else -1
    # Time: O(E * log(V))

# Solution: https://youtu.be/Bp7STMWMMQw
# Credit: Greg Hogg
def network_delay_time_alt(times, n, k):
    # Djikstra's Algorithm
    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append((v, time))
    
    min_times = {}
    min_heap = [(0, k)] # (distance from source to node, node)

    while min_heap:
        time_k_to_i, i = heapq.heappop(min_heap)
        if i in min_times:
            continue
        
        min_times[i] = time_k_to_i
        for nei, nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
    
    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1
    # Time: O((V + E) log (V))
    # Space: O(V + E)

def main():
    result = network_delay_time(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    print(result) # 2

    result = network_delay_time(times = [[1,2,1]], n = 2, k = 1)
    print(result) # 1

    result = network_delay_time(times = [[1,2,1]], n = 2, k = 2)
    print(result) # -1

if __name__ == "__main__":
    main()

# ----------------------------------
# 1514. Path With Maximum Probability
# ----------------------------------

# Problem: https://leetcode.com/problems/path-with-maximum-probability
#
# You are given an undirected weighted graph of n nodes (0-indexed), represented
# by an edge list where edges[i] = [a, b] is an undirected edge connecting the
# nodes a and b with a probability of success of traversing that edge succProb[i].
# 
# Given two nodes start and end, find the path with the maximum probability of
# success to go from start to end and return its success probability.
# 
# If there is no path from start to end, return 0. Your answer will be accepted if
# it differs from the correct answer by at most 1e-5.
# 
# Example 1:
# 
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0,
# end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of
# success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# 
# Example 2:
# 
# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0,
# end = 2
# Output: 0.30000
# 
# Example 3:
# 
# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
# 
# 
# Constraints:
#         2 <= n <= 10^4
#         0 <= start, end < n
#         start != end
#         0 <= a, b < n
#         a != b
#         0 <= succProb.length == edges.length <= 2*10^4
#         0 <= succProb[i] <= 1
#         There is at most one edge between every two nodes.

import collections
import heapq

# Solution: https://youtu.be/kPsDTGcrzGM
# Credit: Navdeep Singh founder of NeetCode
def max_probability(n, edges, succProb, start, end):
    adj = collections.defaultdict(list)
    for i in range(len(edges)):
        src, dst = edges[i]
        adj[src].append([dst, succProb[i]])
        adj[dst].append([src, succProb[i]])

    pq = [(-1, start)]
    visit = set()

    while pq:
        prob, cur = heapq.heappop(pq)
        visit.add(cur)

        if cur == end:
            return prob * -1
        for nei, edgeProb in adj[cur]:
            if nei not in visit:
                heapq.heappush(pq, (prob * edgeProb, nei))
    return 0


def main():
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    result = max_probability(3, edges, succProb, 0, 2)
    print(result) # 0.25

    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.3]
    result = max_probability(3, edges, succProb, 0, 2)
    print(result) # 0.3

    edges = [[0,1]]
    succProb = [0.5]
    result = max_probability(3, edges, succProb, 0, 2)
    print(result) # 0

if __name__ == "__main__":
    main()

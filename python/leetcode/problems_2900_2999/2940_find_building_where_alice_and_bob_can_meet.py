# ------------------------------------------------
# 2940. Find Building Where Alice and Bob Can Meet
# ------------------------------------------------

# Problem: https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet
#
# You are given a 0-indexed array heights of positive integers, where heights[i]
# represents the height of the ith building.
# 
# If a person is in building i, they can move to any other building j if and only
# if i < j and heights[i] < heights[j].
# 
# You are also given another array queries where queries[i] = [ai, bi]. On the ith
# query, Alice is in building ai while Bob is in building bi.
# 
# Return an array ans where ans[i] is the index of the leftmost building where
# Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a
# common building on query i, set ans[i] to -1.
# 
# Example 1:
# 
# Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# Output: [2,5,-1,5,2]
# 
# Explanation: In the first query, Alice and Bob can move to building 2 since
# heights[0] < heights[2] and heights[1] < heights[2].
# In the second query, Alice and Bob can move to building 5 since heights[0] <
# heights[5] and heights[3] < heights[5].
# In the third query, Alice cannot meet Bob since Alice cannot move to any other
# building.
# In the fourth query, Alice and Bob can move to building 5 since heights[3] <
# heights[5] and heights[4] < heights[5].
# In the fifth query, Alice and Bob are already in the same building.
# For ans[i] != -1, It can be shown that ans[i] is the leftmost building where
# Alice and Bob can meet.
# For ans[i] == -1, It can be shown that there is no building where Alice and Bob
# can meet.
# 
# Example 2:
# 
# Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
# Output: [7,6,-1,4,6]
# 
# Explanation: In the first query, Alice can directly move to Bob's building since
# heights[0] < heights[7].
# In the second query, Alice and Bob can move to building 6 since heights[3] <
# heights[6] and heights[5] < heights[6].
# In the third query, Alice cannot meet Bob since Bob cannot move to any other
# building.
# In the fourth query, Alice and Bob can move to building 4 since heights[3] <
# heights[4] and heights[0] < heights[4].
# In the fifth query, Alice can directly move to Bob's building since heights[1] <
# heights[6].
# For ans[i] != -1, It can be shown that ans[i] is the leftmost building where
# Alice and Bob can meet.
# For ans[i] == -1, It can be shown that there is no building where Alice and Bob
# can meet.
# 
# Constraints:
#         1 <= heights.length <= 5 * 10^4
#         1 <= heights[i] <= 10^9
#         1 <= queries.length <= 5 * 10^4
#         queries[i] = [ai, bi]
#         0 <= ai, bi <= heights.length - 1

from collections import defaultdict
import heapq

# Solution: https://youtu.be/HJaSuUOUH90
# Credit: Navdeep Singh founder of NeetCode
def leftmost_building_queries(heights, queries):
    res = [-1] * len(queries)
    groups = defaultdict(list)
    for i, q in enumerate(queries):
        l, r = sorted(q)
        if l == r or heights[r] > heights[l]:
            res[i] = r
        else:
            h = max(heights[l], heights[r])
            groups[r].append((h, i))
    min_heap = []
    for i, h in enumerate(heights):
        for q_h, q_i in groups[i]:
            heapq.heappush(min_heap, (q_h, q_i))
        while min_heap and h > min_heap[0][0]:
            q_h, q_i = heapq.heappop(min_heap)
            res[q_i] = i
    return res
    # Time: O(n + q * log(q)) n = buildings and q = queries
    # Space: O(q)


def main():
    result = leftmost_building_queries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]])
    print(result) # [2,5,-1,5,2]

    result = leftmost_building_queries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])
    print(result) # [7,6,-1,4,6]

if __name__ == "__main__":
    main()

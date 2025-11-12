# ------------------
# 1345. Jump Game IV
# ------------------

# Problem: https://leetcode.com/problems/jump-game-iv
#
# Given an array of integers arr, you are initially positioned at the first index
# of the array.
# 
# In one step you can jump from index i to index:
#         i + 1 where: i + 1 < arr.length.
#         i - 1 where: i - 1 >= 0.
#         j where: arr[i] == arr[j] and i != j.
# 
# Return the minimum number of steps to reach the last index of the array.
# 
# Notice that you can not jump outside of the array at any time.
# 
# Example 1:
# 
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
# index 9 is the last index of the array.
# 
# Example 2:
# 
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
# 
# Example 3:
# 
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index
# of the array.
# 
# 
# Constraints:
#         1 <= arr.length <= 5 * 10^4
#         -10^8 <= arr[i] <= 10^8


# Solution: https://youtu.be/1LXhkTWAW74
# Credit: Navdeep Singh founder of NeetCode
from collections import defaultdict, deque
from typing import List

class Solution:
    # Time O(n) - Space O(n)
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # Base case.
        if n < 2:
            return 0
        # A dictionary of vertices indexed by values.
        d = defaultdict(list)
        for i in reversed(range(n)):
            d[arr[i]].append(i)

        # A function that gets all neighbors of a node that we have not
        # queued yet.
        def getUnqueuedNeighbors(i: int) -> List[int]:
            adj = []
            # We can reach the element before.
            if 0 < i and not seen[i - 1]:
                seen[i - 1] = True
                adj.append(i - 1)
            # We can reach the element after.
            if i < n - 1 and not seen[i + 1]:
                seen[i + 1] = True
                adj.append(i + 1)
            # We can also reach any element with the same value.
            if arr[i] in d:
                for node in d[arr[i]]:
                    if node != i:
                        adj.append(node)
                        seen[node] = True
                d.pop(arr[i])
            return adj

        # A list of nodes that we have visited already.
        seen = [False] * n
        seen[0] = True
        # BFS starting at 0 and counting the steps until we reach n-1.
        steps, level = 0, deque([0])
        while level:
            steps += 1
            # Process an entire level.
            for _ in range(len(level)):
                current = level.popleft()
                for nei in getUnqueuedNeighbors(current):
                    # If this is the target node, return.
                    if nei == n - 1:
                        return steps
                    level.append(nei)

def main():
    print("TO DO")

if __name__ == "__main__":
    main()

# -------------------
# 1306. Jump Game III
# -------------------

# Problem: https://leetcode.com/problems/jump-game-iii
#
# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i] or
# i - arr[i], check if you can reach any index with value 0.
# 
# Notice that you can not jump outside of the array at any time.
# 
# Example 1:
# 
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# 
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
# 
# Example 2:
# 
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# 
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
# 
# Example 3:
# 
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# 
# Explanation: There is no way to reach at index 1 with value 0.
# 
# 
# Constraints:
#         1 <= arr.length <= 5 * 10⁴
#         0 <= arr[i] < arr.length
#         0 <= start < arr.length

from collections import deque

# Solution: https://algo.monster/liteproblems/1306
# Credit: AlgoMonster
def can_reach(arr, start):
    # Initialize BFS queue with starting position
    queue = deque([start])
    
    # BFS traversal to find if we can reach value 0
    while queue:
        # Get current index from queue
        current_index = queue.popleft()
        
        # Check if we've reached target (value is 0)
        if arr[current_index] == 0:
            return True
        
        # Store jump distance before marking as visited
        jump_distance = arr[current_index]
        
        # Mark current index as visited by setting to -1
        arr[current_index] = -1
        
        # Try both possible jumps: forward and backward
        for next_index in (current_index + jump_distance, current_index - jump_distance):
            # Check if next index is valid and unvisited
            # arr[next_index] >= 0 ensures we haven't visited it yet (unvisited values are non-negative)
            if 0 <= next_index < len(arr) and arr[next_index] >= 0:
                queue.append(next_index)
    
    # No path to index with value 0 found
    return False
    # Time: O(n)
    # Space: O(n)


def main():
    result = can_reach(arr = [4,2,3,0,3,1,2], start = 5)
    print(result) # True

    result = can_reach(arr = [4,2,3,0,3,1,2], start = 0)
    print(result) # True

    result = can_reach(arr = [3,0,2,1,2], start = 2)
    print(result) # False

if __name__ == "__main__":
    main()

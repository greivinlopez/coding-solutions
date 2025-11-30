# ------------------
# 1696. Jump Game VI
# ------------------

# Problem: https://leetcode.com/problems/jump-game-vi
#
# You are given a 0-indexed integer array nums and an integer k.
# 
# You are initially standing at index 0. In one move, you can jump at most k steps
# forward without going outside the boundaries of the array. That is, you can jump
# from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
# 
# You want to reach the last index of the array (index n - 1). Your score is the
# sum of all nums[j] for each index j you visited in the array.
# 
# Return the maximum score you can get.
# 
# Example 1:
# 
# Input: nums = [1,-1,-2,4,-7,3], k = 2
# Output: 7
# 
# Explanation: You can choose your jumps forming the subsequence [1,-1,4,3]
# (underlined above). The sum is 7.
# 
# Example 2:
# 
# Input: nums = [10,-5,-2,4,0,3], k = 3
# Output: 17
# 
# Explanation: You can choose your jumps forming the subsequence [10,4,3]
# (underlined above). The sum is 17.
# 
# Example 3:
# 
# Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
# Output: 0
# 
# 
# Constraints:
#         1 <= nums.length, k <= 10⁵
#         -10⁴ <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1696
# Credit: AlgoMonster
def max_result(nums, k):
    from collections import deque

    n = len(nums)
    
    # dp[i] represents the maximum score when reaching index i
    dp = [0] * n
    
    # Monotonic deque to maintain indices of potential maximum values
    # within the sliding window of size k
    deque_indices = deque([0])
    
    for i in range(n):
        # Remove indices that are outside the valid jump range (window size k)
        if i - deque_indices[0] > k:
            deque_indices.popleft()
        
        # Calculate maximum score for current position:
        # current value + best score from a reachable previous position
        dp[i] = nums[i] + dp[deque_indices[0]]
        
        # Maintain monotonic decreasing property of the deque
        # Remove indices with smaller or equal dp values from the back
        while deque_indices and dp[deque_indices[-1]] <= dp[i]:
            deque_indices.pop()
        
        # Add current index to the deque
        deque_indices.append(i)
    
    # Return the maximum score when reaching the last position
    return dp[-1]
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_result(nums = [1,-1,-2,4,-7,3], k = 2)
    print(result) # 7

    result = max_result(nums = [10,-5,-2,4,0,3], k = 3)
    print(result) # 17

    result = max_result(nums = [1,-5,-20,4,-1,3,-6,-3], k = 2)
    print(result) # 0

if __name__ == "__main__":
    main()

# ------------------------------------------
# 862. Shortest Subarray With Sum At Least K
# ------------------------------------------

# Problem: https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# 
# Given an integer array nums and an integer k, return the length of the 
# shortest non-empty subarray of nums with a sum of at least k. If there is no 
# such subarray, return -1.
# 
# A subarray is a contiguous part of an array.
# 
#  
# Example 1:
# 
# Input: nums = [1], k = 1
# Output: 1
# 
# Example 2:
# 
# Input: nums = [1,2], k = 4
# Output: -1
# 
# Example 3:
# 
# Input: nums = [2,-1,2], k = 3
# Output: 3
#  
# 
# Constraints:
# 
#   1 <= nums.length <= 10^5
#   -10^5 <= nums[i] <= 10^5
#   1 <= k <= 10^9

import collections

# Solution: https://youtu.be/5AY70aAHZiQ
# Credit: Navdeep Singh founder of NeetCode
def shortest_subarray(nums, k):
    size = len(nums)
    pre = [0]
    for i in nums:
        pre.append(pre[-1] + i)

    ans = size + 1
    monoq = collections.deque()
    for i, val in enumerate(pre):
        while monoq and val <= pre[monoq[-1]]:
            monoq.pop()
        while monoq and val - pre[monoq[0]] >= k:
            ans = min(ans, i - monoq.popleft())
        
        monoq.append(i)
    
    return ans if ans < size + 1 else -1 


def main():
    result = shortest_subarray(nums = [1], k = 1)
    print(result) # 1

    result = shortest_subarray(nums = [1,2], k = 4)
    print(result) # -1

    result = shortest_subarray(nums = [2,-1,2], k = 3)
    print(result) # 3

if __name__ == "__main__":
    main()

# -------------------------------------------
# 1673. Find the Most Competitive Subsequence
# -------------------------------------------

# Problem: https://leetcode.com/problems/find-the-most-competitive-subsequence
#
# Given an integer array nums and a positive integer k, return the most
# competitive subsequence of nums of size k.
# 
# An array's subsequence is a resulting sequence obtained by erasing some
# (possibly zero) elements from the array.
# 
# We define that a subsequence a is more competitive than a subsequence b (of the
# same length) if in the first position where a and b differ, subsequence a has a
# number less than the corresponding number in b. For example, [1,3,4] is more
# competitive than [1,3,5] because the first position they differ is at the final
# number, and 4 is less than 5.
# 
# Example 1:
# 
# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]
# 
# Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6],
# [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
# 
# Example 2:
# 
# Input: nums = [2,4,3,3,5,4,9,6], k = 4
# Output: [2,3,3,4]
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁹
#         1 <= k <= nums.length


# Solution: https://algo.monster/liteproblems/1673
# Credit: AlgoMonster
def most_competitive(nums, k):
    # Use a monotonic stack to maintain the smallest possible subsequence
    stack = []
    n = len(nums)
    
    # Process each element in the array
    for index, value in enumerate(nums):
        # Remove larger elements from stack if we have enough remaining elements
        # to fill up to k elements total
        # Condition: stack[-1] > value ensures we only remove larger elements
        # Condition: len(stack) + n - index > k ensures we have enough elements left
        while stack and stack[-1] > value and len(stack) + n - index > k:
            stack.pop()
        
        # Only add elements if we haven't reached k elements yet
        if len(stack) < k:
            stack.append(value)
    
    return stack
    # Time: O(n)
    # Space: O(k)
    # k = the desired size of the most competitive subsequence.


def main():
    result = most_competitive(nums = [3,5,2,6], k = 2)
    print(result) # [2, 6]

    result = most_competitive(nums = [2,4,3,3,5,4,9,6], k = 4)
    print(result) # [2, 3, 3, 4]

if __name__ == "__main__":
    main()

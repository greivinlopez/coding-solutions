# -----------------------------
# 368. Largest Divisible Subset
# -----------------------------

# Problem: https://leetcode.com/problems/largest-divisible-subset
#
# Given a set of distinct positive integers nums, return the largest subset answer
# such that every pair (answer[i], answer[j]) of elements in this subset
# satisfies:
# 
#         answer[i] % answer[j] == 0, or
#         answer[j] % answer[i] == 0
# 
# If there are multiple solutions, return any of them.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [1,2]
# 
# Explanation: [1,3] is also accepted.
# 
# Example 2:
# 
# Input: nums = [1,2,4,8]
# Output: [1,2,4,8]
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= 2 * 10^9
#         All the integers in nums are unique.


# Solution: https://youtu.be/O-aXzrDB49w
# Credit: Navdeep Singh founder of NeetCode
def largest_divisible_subset(nums):
    nums.sort()
    cache = {}

    def dfs(i):
        if i in cache:
            return cache[i]
        if i == len(nums):
            return []

        res = [nums[i]]
        for j in range(i + 1, len(nums)):
            if nums[j] % nums[i] == 0:
                tmp = [nums[i]] + dfs(j)
                if len(tmp) > len(res):
                    res = tmp
        
        cache[i] = res
        return res

    res = []
    for i in range(len(nums)):
        tmp = dfs(i)
        if len(tmp) > len(res):
            res = tmp
    
    return res
    # Time: O(n ^ 2)
    # Space: O(n)

def main():
    result = largest_divisible_subset([1,2,3])
    print(result) # [1,2] or [1,3]

    result = largest_divisible_subset([1,2,4,8])
    print(result) # [1,2,4,8]

if __name__ == "__main__":
    main()

# ------------------------------------------------
# 2044. Count Number of Maximum Bitwise-OR Subsets
# ------------------------------------------------

# Problem: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets
#
# Given an integer array nums, find the maximum possible bitwise OR of a subset of
# nums and return the number of different non-empty subsets with the maximum
# bitwise OR.
# 
# An array a is a subset of an array b if a can be obtained from b by deleting
# some (possibly zero) elements of b. Two subsets are considered different if the
# indices of the elements chosen are different.
# 
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1]
# (0-indexed).
# 
# Example 1:
# 
# Input: nums = [3,1]
# Output: 2
# 
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2
# subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
# 
# Example 2:
# 
# Input: nums = [2,2,2]
# Output: 7
# 
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are
# 23 - 1 = 7 total subsets.
# 
# Example 3:
# 
# Input: nums = [3,2,1,5]
# Output: 6
# 
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6
# subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]
# 
# 
# Constraints:
#         1 <= nums.length <= 16
#         1 <= nums[i] <= 10^5


# Solution: https://youtu.be/_wBj3IMV7tY
# Credit: Navdeep Singh founder of NeetCode
def count_max_or_subsets_brute(nums):
    # Brute force
    max_or = 0
    for n in nums:
        max_or |= n

    def dfs(i, cur_or):
        nonlocal max_or
        if i == len(nums):
            return 1 if cur_or == max_or else 0

        return (
            dfs(i + 1, cur_or) +
            dfs(i + 1, cur_or | nums[i])
        )

    return dfs(0, 0)
    # Time: O(2^n)

def count_max_or_subsets_memo(nums):
    # Memoization
    max_or = 0
    for n in nums:
        max_or |= n

    cache = [[-1] * (max_or + 1) for _ in range(len(nums))]

    def dfs(i, cur_or):
        nonlocal max_or
        if i == len(nums):
            return 1 if cur_or == max_or else 0
        
        if cache[i][cur_or] != -1:
            return cache[i][cur_or]

        cache[i][cur_or] = (
            dfs(i + 1, cur_or) +
            dfs(i + 1, cur_or | nums[i])
        )

        return cache[i][cur_or]

    return dfs(0, 0)


def count_max_or_subsets(nums):
    # Bottom up
    max_or_value = 0
    dp = [0] * (1 << 17)
    
    # Initialize the empty subset
    dp[0] = 1

    # Iterate through each number in the input array
    for num in nums:
        for i in range(max_or_value, -1, -1):
            # For each existing subset, create a new subset by including the current number
            dp[i | num] += dp[i]
        
        # Update the maximum OR value
        max_or_value |= num

    return dp[max_or_value]
    # Time: O(n * max) 

def count_max_or_subsets_bitmask(nums):
    max_or = 0
    for n in nums:
        max_or |= n

    length = len(nums)
    res = 0

    for subset in range(1, 2**length):
        cur_or = 0
        for i in range(length):
            if (1 << i) & subset:
                cur_or |= nums[i]
        res += 1 if cur_or == max_or else 0
    
    return res
    # Time: O(n * 2^n)
    # Space: O(1)

def main():
    result = count_max_or_subsets([3,1])
    print(result) # 2

    result = count_max_or_subsets([2,2,2])
    print(result) # 7

    result = count_max_or_subsets([3,2,1,5])
    print(result) # 6

if __name__ == "__main__":
    main()

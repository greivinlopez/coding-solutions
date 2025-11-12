# --------------------------------------------------------
# 1218. Longest Arithmetic Subsequence of Given Difference
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference
#
# Given an integer array arr and an integer difference, return the length of the
# longest subsequence in arr which is an arithmetic sequence such that the
# difference between adjacent elements in the subsequence equals difference.
# 
# A subsequence is a sequence that can be derived from arr by deleting some or no
# elements without changing the order of the remaining elements.
# 
# Example 1:
# 
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# 
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
# 
# Example 2:
# 
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# 
# Explanation: The longest arithmetic subsequence is any single element.
# 
# Example 3:
# 
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# 
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         -10⁴ <= arr[i], difference <= 10⁴

from collections import defaultdict

# Solution: https://algo.monster/liteproblems/1218
# Credit: AlgoMonster
def longest_subsequence(arr, difference):
    # Dictionary to store the length of longest arithmetic subsequence ending at each value
    # Key: array element value, Value: length of longest subsequence ending at this value
    dp = defaultdict(int)
    
    # Iterate through each element in the array
    for num in arr:
        # For current number, the longest subsequence ending at it equals:
        # 1 + length of longest subsequence ending at (num - difference)
        # This works because we need consecutive elements to differ by 'difference'
        dp[num] = dp[num - difference] + 1
    
    # Return the maximum length among all subsequences
    return max(dp.values())
    # Time: O(n)
    # Space: O(n)


def main():
    result = longest_subsequence(arr = [1,2,3,4], difference = 1)
    print(result) # 4

    result = longest_subsequence(arr = [1,3,5,7], difference = 1)
    print(result) # 1

    result = longest_subsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2)
    print(result) # 4

if __name__ == "__main__":
    main()

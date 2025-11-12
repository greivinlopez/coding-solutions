# ---------------------------------
# 845. Longest Mountain in Array ⛰️
# ---------------------------------

# Problem: https://leetcode.com/problems/longest-mountain-in-array
#
# You may recall that an array arr is a mountain array if and only if:
#         
#   * arr.length >= 3
#   * There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
#       * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#       * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# Given an integer array arr, return the length of the longest subarray, which is
# a mountain. Return 0 if there is no mountain subarray.
# 
# Example 1:
# 
# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# 
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# 
# Example 2:
# 
# Input: arr = [2,2,2]
# Output: 0
# 
# Explanation: There is no mountain.
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         0 <= arr[i] <= 10⁴
# 
# Follow up:
#         Can you solve it using only one pass?
#         Can you solve it in O(1) space?


# Solution: https://algo.monster/liteproblems/845
# Credit: AlgoMonster
def longest_mountain(arr):
    n = len(arr)
    
    # left[i] stores the length of increasing sequence ending at index i
    left = [1] * n
    
    # right[i] stores the length of decreasing sequence starting at index i
    right = [1] * n
    
    # Build left array: count consecutive increasing elements from left
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            left[i] = left[i - 1] + 1
    
    max_length = 0
    
    # Build right array: count consecutive decreasing elements from right
    # and calculate the mountain length at the same time
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            right[i] = right[i + 1] + 1
            
            # Valid mountain requires uphill (left[i] > 1) and downhill (right[i] > 1)
            if left[i] > 1:
                # Mountain length = uphill + downhill - 1 (peak counted twice)
                max_length = max(max_length, left[i] + right[i] - 1)
    
    return max_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = longest_mountain(arr = [2,1,4,7,3,2,5])
    print(result) # 5

    result = longest_mountain(arr = [2,2,2])
    print(result) # 0

if __name__ == "__main__":
    main()

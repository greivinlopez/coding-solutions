# --------------------------------------------
# 1186. Maximum Subarray Sum with One Deletion
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining elements
# is maximum possible.
# 
# Note that the subarray needs to be non-empty after deleting one element.
# 
# Example 1:
# 
# Input: arr = [1,-2,0,3]
# Output: 4
# 
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray
# [1, 0, 3] becomes the maximum value.
# 
# Example 2:
# 
# Input: arr = [1,-2,-2,3]
# Output: 3
# 
# Explanation: We just choose [3] and it's the maximum sum.
# 
# Example 3:
# 
# Input: arr = [-1,-1,-1,-1]
# Output: -1
# 
# Explanation: The final subarray needs to be non-empty. You can't choose [-1] and
# delete -1 from it, then get an empty subarray to make the sum equals to 0.
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         -10⁴ <= arr[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1186
# Credit: AlgoMonster
def maximum_sum_alt(arr):
    n = len(arr)
    
    # left[i] stores the maximum subarray sum ending at index i
    max_sum_ending_here_left = [0] * n
    
    # right[i] stores the maximum subarray sum starting at index i
    max_sum_starting_here_right = [0] * n
    
    # Build the left array using Kadane's algorithm from left to right
    current_sum = 0
    for i in range(n):
        current_sum = max(current_sum, 0) + arr[i]
        max_sum_ending_here_left[i] = current_sum
    
    # Build the right array using Kadane's algorithm from right to left
    current_sum = 0
    for i in range(n - 1, -1, -1):
        current_sum = max(current_sum, 0) + arr[i]
        max_sum_starting_here_right[i] = current_sum
    
    # Initialize answer with maximum subarray sum without deletion
    max_result = max(max_sum_ending_here_left)
    
    # Try deleting each element (except first and last) and calculate the sum
    # by connecting the maximum subarray ending before it with the maximum
    # subarray starting after it
    for i in range(1, n - 1):
        max_result = max(max_result, 
                        max_sum_ending_here_left[i - 1] + max_sum_starting_here_right[i + 1])
    
    return max_result
    # Time: O(n)
    # Space: O(n)

# Alternative Solution: Kadane's algorithm
# Solution: https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/solutions/4418847/simple-5-line-kadane-s-algorithm-beats-91-82
# Credit: Suyash -> https://leetcode.com/u/Suyash4396/
def maximum_sum(arr):
    cur_sum_no_del = cur_sum_del = max_sum = arr[0]

    for i in range(1, len(arr)):  # Changed: no slicing
        num = arr[i]
        cur_sum_del = max(cur_sum_del + num, num, cur_sum_no_del)
        cur_sum_no_del = max(cur_sum_no_del + num, num)
        max_sum = max(max_sum, cur_sum_no_del, cur_sum_del)

    return max_sum
    # Time: O(n)
    # Space: O(1)


def main():
    result = maximum_sum(arr = [1,-2,0,3])
    print(result) # 4

    result = maximum_sum(arr = [1,-2,-2,3])
    print(result) # 3

    result = maximum_sum(arr = [-1,-1,-1,-1])
    print(result) # -1

if __name__ == "__main__":
    main()

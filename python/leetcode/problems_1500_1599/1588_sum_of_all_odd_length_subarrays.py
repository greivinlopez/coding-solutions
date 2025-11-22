# -------------------------------------
# 1588. Sum of All Odd Length Subarrays
# -------------------------------------

# Problem: https://leetcode.com/problems/sum-of-all-odd-length-subarrays
#
# Given an array of positive integers arr, return the sum of all possible odd-
# length subarrays of arr.
# 
# A subarray is a contiguous subsequence of the array.
# 
# Example 1:
# 
# Input: arr = [1,4,2,5,3]
# Output: 58
# 
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
# 
# Example 2:
# 
# Input: arr = [1,2]
# Output: 3
# 
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is
# 3.
# 
# Example 3:
# 
# Input: arr = [10,11,12]
# Output: 66
# 
# 
# Constraints:
#         1 <= arr.length <= 100
#         1 <= arr[i] <= 1000
# 
# Follow up:
# Could you solve this problem in O(n) time complexity?


# Solution: https://algo.monster/liteproblems/1588
# Credit: AlgoMonster
def sum_odd_length_subarrays_alt(arr):
    n = len(arr)
    
    # odd_sum[i]: sum of all odd-length subarrays ending at index i
    odd_sum = [0] * n
    
    # even_sum[i]: sum of all even-length subarrays ending at index i
    even_sum = [0] * n
    
    # Initialize: single element at index 0 forms an odd-length subarray (length 1)
    total_sum = odd_sum[0] = arr[0]
    
    # Process each element starting from index 1
    for i in range(1, n):
        # Calculate sum of odd-length subarrays ending at index i
        # Uses previous even-length subarrays and extends them by one element
        # The count of such subarrays is (i // 2 + 1)
        odd_sum[i] = even_sum[i - 1] + arr[i] * (i // 2 + 1)
        
        # Calculate sum of even-length subarrays ending at index i
        # Uses previous odd-length subarrays and extends them by one element
        # The count of such subarrays is ((i + 1) // 2)
        even_sum[i] = odd_sum[i - 1] + arr[i] * ((i + 1) // 2)
        
        # Add current odd-length subarray sums to the total
        total_sum += odd_sum[i]
    
    return total_sum
    # Time: O(n)
    # Space: O(n)


# My Solution
def sum_odd_length_subarrays(arr):
    total_sum = 0
    n = len(arr)
    
    for i in range(n):
        total_subarrays_containing_i = (i + 1) * (n - i)
        # Formula: (total + 1) // 2
        odd_subarrays_count = (total_subarrays_containing_i + 1) // 2
        # Add the contribution of this number to the total
        total_sum += arr[i] * odd_subarrays_count
        
    return total_sum
    # Time: O(n)
    # Space: O(1)


def main():
    result = sum_odd_length_subarrays(arr = [1,4,2,5,3])
    print(result) # True

    result = sum_odd_length_subarrays(arr = [1,2])
    print(result) # True

    result = sum_odd_length_subarrays(arr = [10,11,12])
    print(result) # False

if __name__ == "__main__":
    main()

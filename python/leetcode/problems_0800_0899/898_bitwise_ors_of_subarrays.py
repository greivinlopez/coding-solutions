# -----------------------------
# 898. Bitwise ORs of Subarrays
# -----------------------------

# Problem: https://leetcode.com/problems/bitwise-ors-of-subarrays
#
# Given an integer array arr, return the number of distinct bitwise ORs of all the
# non-empty subarrays of arr.
# 
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray.
# The bitwise OR of a subarray of one integer is that integer.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
# Example 1:
# 
# Input: arr = [0]
# Output: 1
# 
# Explanation: There is only one possible result: 0.
# 
# Example 2:
# 
# Input: arr = [1,1,2]
# Output: 3
# 
# Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1,
# 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
# 
# Example 3:
# 
# Input: arr = [1,2,4]
# Output: 6
# 
# Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
# 
# 
# Constraints:
#         1 <= arr.length <= 5 * 10⁴
#         0 <= arr[i] <= 10⁹


# Solution: https://algo.monster/liteproblems/898
# Credit: AlgoMonster
def subarray_bitwise_ORs(arr):
    # Set to store all unique bitwise OR results from all subarrays
    all_results = set()
    
    # Set to store bitwise OR results ending at current position
    current_ending_here = set()
    
    # Iterate through each element in the array
    for num in arr:
        # Calculate new set of OR values by:
        # 1. OR-ing current number with all values ending at previous position
        # 2. Including the current number itself as a subarray of length 1
        current_ending_here = {num | prev_value for prev_value in current_ending_here} | {num}
        
        # Add all OR values ending at current position to the final result set
        all_results |= current_ending_here
    
    # Return the count of unique bitwise OR values
    return len(all_results)
    # Time: O(n * log(m))
    # Space: O(n * log(m))
    # n = number of elements in array
    # m = the maximum value in the array.


def main():
    result = subarray_bitwise_ORs(arr = [0])
    print(result) # 1

    result = subarray_bitwise_ORs(arr = [1,1,2])
    print(result) # 3

    result = subarray_bitwise_ORs(arr = [1,2,4])
    print(result) # 6

if __name__ == "__main__":
    main()

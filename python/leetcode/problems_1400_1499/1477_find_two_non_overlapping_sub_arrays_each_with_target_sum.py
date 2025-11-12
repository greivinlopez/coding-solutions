# --------------------------------------------------------------
# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
# --------------------------------------------------------------

# Problem: https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum
#
# You are given an array of integers arr and an integer target.
# 
# You have to find two non-overlapping sub-arrays of arr each with a sum equal
# target. There can be multiple answers so you have to find an answer where the
# sum of the lengths of the two sub-arrays is minimum.
# 
# Return the minimum sum of the lengths of the two required sub-arrays, or return
# -1 if you cannot find such two sub-arrays.
# 
# Example 1:
# 
# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# 
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their
# lengths is 2.
# 
# Example 2:
# 
# Input: arr = [7,3,4,7], target = 7
# Output: 2
# 
# Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7],
# [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of
# their lengths is 2.
# 
# Example 3:
# 
# Input: arr = [4,3,2,6,2,3,4], target = 6
# Output: -1
# 
# Explanation: We have only one sub-array of sum = 6.
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         1 <= arr[i] <= 1000
#         1 <= target <= 10⁸


# Solution: https://algo.monster/liteproblems/1477
# Credit: AlgoMonster
def min_sum_of_lengths(arr, target):
    # Dictionary to store cumulative sum -> index mapping
    # Key: cumulative sum, Value: index (1-indexed)
    cumsum_to_index = {0: 0}
    
    cumulative_sum = 0
    array_length = len(arr)
    
    # min_length[i] stores the minimum length of a subarray ending at or before index i
    # that sums to target (initialized to infinity)
    min_length = [float('inf')] * (array_length + 1)
    
    # Track the minimum sum of two subarray lengths
    min_total_length = float('inf')
    
    # Iterate through array with 1-based indexing
    for current_index, current_value in enumerate(arr, 1):
        cumulative_sum += current_value
        
        # Carry forward the minimum length from previous position
        min_length[current_index] = min_length[current_index - 1]
        
        # Check if we can form a subarray ending at current position that sums to target
        # We need cumulative_sum - target to exist in our dictionary
        required_sum = cumulative_sum - target
        
        if required_sum in cumsum_to_index:
            # Found a valid subarray from start_index to current_index
            start_index = cumsum_to_index[required_sum]
            current_subarray_length = current_index - start_index
            
            # Update minimum length for subarrays ending at or before current position
            min_length[current_index] = min(min_length[current_index], current_subarray_length)
            
            # Try to combine with best subarray ending before start_index
            # min_length[start_index] gives us the best subarray before current one
            combined_length = min_length[start_index] + current_subarray_length
            min_total_length = min(min_total_length, combined_length)
        
        # Store current cumulative sum and its index
        cumsum_to_index[cumulative_sum] = current_index
    
    # Return -1 if no valid pair found, otherwise return minimum total length
    return -1 if min_total_length > array_length else min_total_length
    # Time: O(n)
    # Space: O(n)


def main():
    result = min_sum_of_lengths(arr = [3,2,2,4,3], target = 3)
    print(result) # 2

    result = min_sum_of_lengths(arr = [7,3,4,7], target = 7)
    print(result) # 2

    result = min_sum_of_lengths(arr = [4,3,2,6,2,3,4], target = 6)
    print(result) # -1

if __name__ == "__main__":
    main()

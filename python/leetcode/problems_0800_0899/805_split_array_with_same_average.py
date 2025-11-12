# ----------------------------------
# 805. Split Array With Same Average
# ----------------------------------

# Problem: https://leetcode.com/problems/split-array-with-same-average
#
# You are given an integer array nums.
# 
# You should move each element of nums into one of the two arrays A and B such
# that A and B are non-empty, and average(A) == average(B).
# 
# Return true if it is possible to achieve that and false otherwise.
# 
# Note that for an array arr, average(arr) is the sum of all the elements of arr
# over the length of arr.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4,5,6,7,8]
# Output: true
# 
# Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of
# them have an average of 4.5.
# 
# Example 2:
# 
# Input: nums = [3,1]
# Output: false
# 
# 
# Constraints:
#         1 <= nums.length <= 30
#         0 <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/805
# Credit: AlgoMonster
def split_array_same_average(nums):
    # Get array length
    array_length = len(nums)
    
    # Edge case: cannot split array of size 1
    if array_length == 1:
        return False
    
    # Transform the problem: if we can split into two sets A and B where
    # sum(A)/len(A) = sum(B)/len(B) = total_sum/array_length
    # This is equivalent to: sum(A) * array_length = len(A) * total_sum
    # Rearranging: sum(A * array_length - total_sum) = 0 for each element in A
    total_sum = sum(nums)
    for index, value in enumerate(nums):
        nums[index] = value * array_length - total_sum
    
    # Split array into two halves for meet-in-the-middle approach
    mid_point = array_length >> 1  # equivalent to array_length // 2
    
    # Store all possible sums from the first half
    first_half_sums = set()
    
    # Generate all non-empty subsets of the first half using bit manipulation
    for subset_mask in range(1, 1 << mid_point):
        # Calculate sum of elements in current subset
        subset_sum = sum(
            value 
            for bit_position, value in enumerate(nums[:mid_point]) 
            if subset_mask >> bit_position & 1
        )
        
        # If we found a subset with sum 0, we have a valid split
        if subset_sum == 0:
            return True
        
        # Store this sum for later checking
        first_half_sums.add(subset_sum)
    
    # Generate all non-empty subsets of the second half
    second_half_size = array_length - mid_point
    for subset_mask in range(1, 1 << second_half_size):
        # Calculate sum of elements in current subset
        subset_sum = sum(
            value 
            for bit_position, value in enumerate(nums[mid_point:]) 
            if subset_mask >> bit_position & 1
        )
        
        # Check if this subset alone sums to 0
        if subset_sum == 0:
            return True
        
        # Check if we can combine with a subset from first half to get sum 0
        # But avoid the case where we select all elements (no valid split)
        if subset_mask != (1 << second_half_size) - 1 and -subset_sum in first_half_sums:
            return True
    
    # No valid split found
    return False
    # Time: O(n × 2^(n/2))
    # Space: O(n × 2^(n/2))


def main():
    result = split_array_same_average(nums = [1,2,3,4,5,6,7,8])
    print(result) # True

    result = split_array_same_average(nums = [3,1])
    print(result) # False

if __name__ == "__main__":
    main()

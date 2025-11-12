# ---------------------------------------------
# 795. Number of Subarrays with Bounded Maximum
# ---------------------------------------------

# Problem: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum
#
# Given an integer array nums and two integers left and right, return the number
# of contiguous non-empty subarrays such that the value of the maximum array
# element in that subarray is in the range [left, right].
# 
# The test cases are generated so that the answer will fit in a 32-bit integer.
# 
# Example 1:
# 
# Input: nums = [2,1,4,3], left = 2, right = 3
# Output: 3
# 
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
# [3].
# 
# Example 2:
# 
# Input: nums = [2,9,2,5,6], left = 2, right = 8
# Output: 7
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁹
#         0 <= left <= right <= 10⁹


# Solution: https://algo.monster/liteproblems/795
# Credit: AlgoMonster
def num_subarray_bounded_max(nums, left, right):
    def count_subarrays_with_max_at_most(threshold):
        total_count = 0
        consecutive_valid_elements = 0
        
        for value in nums:
            if value > threshold:
                # Reset the count when we encounter an element > threshold
                consecutive_valid_elements = 0
            else:
                # Increment the count of consecutive valid elements
                consecutive_valid_elements += 1
            
            # Add the number of subarrays ending at current position
            total_count += consecutive_valid_elements
        
        return total_count
    
    # Calculate subarrays with max in range [left, right]
    # This equals: subarrays with max <= right - subarrays with max <= (left - 1)
    subarrays_max_at_most_right = count_subarrays_with_max_at_most(right)
    subarrays_max_less_than_left = count_subarrays_with_max_at_most(left - 1)
    
    return subarrays_max_at_most_right - subarrays_max_less_than_left
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_subarray_bounded_max(nums = [2,1,4,3], left = 2, right = 3)
    print(result) # 3

    result = num_subarray_bounded_max(nums = [2,9,2,5,6], left = 2, right = 8)
    print(result) # 7

if __name__ == "__main__":
    main()

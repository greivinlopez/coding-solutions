# --------------------------------------------
# 1144. Decrease Elements To Make Array Zigzag
# --------------------------------------------

# Problem: https://leetcode.com/problems/decrease-elements-to-make-array-zigzag
#
# Given an array nums of integers, a move consists of choosing any element and
# decreasing it by 1.
# 
# An array A is a zigzag array if either:
#         
#   * Every even-indexed element is greater than adjacent elements, ie. A[0] >
#     A[1] < A[2] > A[3] < A[4] > ...
#   * OR, every odd-indexed element is greater than adjacent elements,
#     ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 
# Return the minimum number of moves to transform the given array nums into a
# zigzag array.
# 
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: 2
# 
# Explanation: We can decrease 2 to 0 or 3 to 1.
# 
# Example 2:
# 
# Input: nums = [9,6,1,6,2]
# Output: 4
# 
# 
# Constraints:
#         1 <= nums.length <= 1000
#         1 <= nums[i] <= 1000


# Solution: https://algo.monster/liteproblems/1144
# Credit: AlgoMonster
def moves_to_make_zigzag(nums):
    # Store moves needed for each pattern:
    # moves_needed[0]: moves to make even indices peaks
    # moves_needed[1]: moves to make odd indices peaks
    moves_needed = [0, 0]
    n = len(nums)
    
    # Try both patterns
    for pattern_type in range(2):
        # Process indices that should be peaks in current pattern
        # pattern_type=0: process even indices (0, 2, 4, ...)
        # pattern_type=1: process odd indices (1, 3, 5, ...)
        for peak_index in range(pattern_type, n, 2):
            # Calculate decrease needed for neighbors to be smaller than current peak
            decrease_amount = 0
            
            # Check left neighbor if it exists
            if peak_index > 0:
                # If left neighbor >= current, need to decrease current
                # by (neighbor_value - current_value + 1) to make current > neighbor
                decrease_amount = max(decrease_amount, nums[peak_index] - nums[peak_index - 1] + 1)
            
            # Check right neighbor if it exists
            if peak_index < n - 1:
                # If right neighbor >= current, need to decrease current
                # by (neighbor_value - current_value + 1) to make current > neighbor
                decrease_amount = max(decrease_amount, nums[peak_index] - nums[peak_index + 1] + 1)
            
            # Add total decrease needed for this index
            moves_needed[pattern_type] += decrease_amount
    
    # Return minimum moves between the two patterns
    return min(moves_needed)
    # Time: O(n)
    # Space: O(1)


def main():
    result = moves_to_make_zigzag(nums = [1,2,3])
    print(result) # 2

    result = moves_to_make_zigzag(nums = [9,6,1,6,2])
    print(result) # 4

if __name__ == "__main__":
    main()

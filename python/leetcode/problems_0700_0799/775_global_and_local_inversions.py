# --------------------------------
# 775. Global and Local Inversions
# --------------------------------

# Problem: https://leetcode.com/problems/global-and-local-inversions
#
# You are given an integer array nums of length n which represents a permutation
# of all the integers in the range [0, n - 1].
# 
# The number of global inversions is the number of the different pairs (i, j)
# where:
# 
#         0 <= i < j < n
#         nums[i] > nums[j]
# 
# The number of local inversions is the number of indices i where:
# 
#         0 <= i < n - 1
#         nums[i] > nums[i + 1]
# 
# Return true if the number of global inversions is equal to the number of local
# inversions.
# 
# Example 1:
# 
# Input: nums = [1,0,2]
# Output: true
# 
# Explanation: There is 1 global inversion and 1 local inversion.
# 
# Example 2:
# 
# Input: nums = [1,2,0]
# Output: false
# 
# Explanation: There are 2 global inversions and 1 local inversion.
# 
# 
# Constraints:
#         n == nums.length
#         1 <= n <= 10⁵
#         0 <= nums[i] < n
#         All the integers of nums are unique.
#         nums is a permutation of all the numbers in the range [0, n - 1].


# Solution: https://algo.monster/liteproblems/775
# Credit: AlgoMonster
def is_ideal_permutation(nums):
    # Track the maximum value seen so far (excluding the previous element)
    max_value = 0
    
    # Start from index 2 to ensure we can look back at nums[i-2]
    for i in range(2, len(nums)):
        # Update max_value to be the maximum of all elements before index i-1
        # This ensures we're checking elements at least 2 positions apart
        max_value = max(max_value, nums[i - 2])
        
        # If any element at least 2 positions back is greater than current element,
        # we have a global inversion that is not a local inversion
        if max_value > nums[i]:
            return False
    
    # All global inversions are also local inversions
    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = is_ideal_permutation(nums = [1,0,2])
    print(result) # True

    result = is_ideal_permutation(nums = [1,2,0])
    print(result) # False

if __name__ == "__main__":
    main()

# -------------------------------
# 1664. Ways to Make a Fair Array
# -------------------------------

# Problem: https://leetcode.com/problems/ways-to-make-a-fair-array
#
# You are given an integer array nums. You can choose exactly one index
# (0-indexed) and remove the element. Notice that the index of the elements may
# change after the removal.
# 
# For example, if nums = [6,1,7,4,1]:
#         
#   * Choosing to remove index 1 results in nums = [6,7,4,1].
#   * Choosing to remove index 2 results in nums = [6,1,4,1].
#   * Choosing to remove index 4 results in nums = [6,1,7,4].
# 
# An array is fair if the sum of the odd-indexed values equals the sum of the
# even-indexed values.
# 
# Return the number of indices that you could choose such that after the removal,
# nums is fair.
# 
# Example 1:
# 
# Input: nums = [2,1,6,4]
# Output: 1
# 
# Explanation:
# Remove index 0: [1,6,4] -> Even sum: 1 + 4 = 5. Odd sum: 6. Not fair.
# Remove index 1: [2,6,4] -> Even sum: 2 + 4 = 6. Odd sum: 6. Fair.
# Remove index 2: [2,1,4] -> Even sum: 2 + 4 = 6. Odd sum: 1. Not fair.
# Remove index 3: [2,1,6] -> Even sum: 2 + 6 = 8. Odd sum: 1. Not fair.
# There is 1 index that you can remove to make nums fair.
# 
# Example 2:
# 
# Input: nums = [1,1,1]
# Output: 3
# 
# Explanation: You can remove any index and the remaining array is fair.
# 
# Example 3:
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# Explanation: You cannot make a fair array after removing any index.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1664
# Credit: AlgoMonster
def ways_to_make_fair(nums):
    # Calculate initial sums of elements at even and odd indices
    even_sum = sum(nums[::2])  # Sum of elements at even indices (0, 2, 4, ...)
    odd_sum = sum(nums[1::2])   # Sum of elements at odd indices (1, 3, 5, ...)
    
    # Initialize counters
    fair_count = 0  # Count of indices that make the array fair when removed
    left_even_sum = 0  # Sum of even-indexed elements to the left of current position
    left_odd_sum = 0   # Sum of odd-indexed elements to the left of current position
    
    # Iterate through each index to check if removing it makes the array fair
    for index, value in enumerate(nums):
        # When we remove an element at index i:
        # - Elements before i keep their parity (even/odd position)
        # - Elements after i switch their parity (even becomes odd, odd becomes even)
        
        if index % 2 == 0:  # Current element is at an even index
            # After removal: 
            # new_even_sum = left_even_sum + (odd_sum - left_odd_sum)
            # new_odd_sum = left_odd_sum + (even_sum - left_even_sum - value)
            if left_odd_sum + even_sum - left_even_sum - value == left_even_sum + odd_sum - left_odd_sum:
                fair_count += 1
            left_even_sum += value
        else:  # Current element is at an odd index
            # After removal:
            # new_even_sum = left_even_sum + (odd_sum - left_odd_sum - value)
            # new_odd_sum = left_odd_sum + (even_sum - left_even_sum)
            if left_odd_sum + even_sum - left_even_sum == left_even_sum + odd_sum - left_odd_sum - value:
                fair_count += 1
            left_odd_sum += value
    
    return fair_count
    # Time: O(n)
    # Space: O(1)


def main():
    result = ways_to_make_fair(nums = [2,1,6,4])
    print(result) # 1

    result = ways_to_make_fair(nums = [1,1,1])
    print(result) # 3

    result = ways_to_make_fair(nums = [1,2,3])
    print(result) # 0

if __name__ == "__main__":
    main()

# ----------------------------
# 922. Sort Array By Parity II
# ----------------------------

# Problem: https://leetcode.com/problems/sort-array-by-parity-ii
#
# Given an array of integers nums, half of the integers in nums are odd, and the
# other half are even.
# 
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i]
# is even, i is even.
# 
# Return any answer array that satisfies this condition.
# 
# Example 1:
# 
# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# 
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# 
# Example 2:
# 
# Input: nums = [2,3]
# Output: [2,3]
# 
# 
# Constraints:
#         2 <= nums.length <= 2 * 10⁴
#         nums.length is even.
#         Half of the integers in nums are even.
#         0 <= nums[i] <= 1000
# 
# Follow Up: Could you solve it in-place?


# Solution: https://algo.monster/liteproblems/922
# Credit: AlgoMonster
def sort_array_by_parity_ii(nums):
    n = len(nums)
    odd_index = 1  # Pointer for odd indices
    
    # Iterate through even indices
    for even_index in range(0, n, 2):
        # If element at even index is odd (violates constraint)
        if nums[even_index] % 2 == 1:
            # Find the next even number at an odd index
            while nums[odd_index] % 2 == 1:
                odd_index += 2
            
            # Swap the misplaced odd number with the misplaced even number
            nums[even_index], nums[odd_index] = nums[odd_index], nums[even_index]
    
    return nums
    # Time: O(n)
    # Space: O(1)


def main():
    result = sort_array_by_parity_ii(nums = [4,2,5,7])
    print(result) # [4, 5, 2, 7]

    result = sort_array_by_parity_ii(nums = [2,3])
    print(result) # [2, 3]

if __name__ == "__main__":
    main()

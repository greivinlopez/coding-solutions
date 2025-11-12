# ------------------------------
# 891. Sum of Subsequence Widths
# ------------------------------

# Problem: https://leetcode.com/problems/sum-of-subsequence-widths
#
# The width of a sequence is the difference between the maximum and minimum
# elements in the sequence.
# 
# Given an array of integers nums, return the sum of the widths of all the non-
# empty subsequences of nums. Since the answer may be very large, return it modulo
# 10⁹ + 7.
# 
# A subsequence is a sequence that can be derived from an array by deleting some
# or no elements without changing the order of the remaining elements. For
# example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 
# Example 1:
# 
# Input: nums = [2,1,3]
# Output: 6
# 
# Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# 
# Example 2:
# 
# Input: nums = [2]
# Output: 0
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         1 <= nums[i] <= 10⁵


# Solution: https://algo.monster/liteproblems/891
# Credit: AlgoMonster
def sum_subseq_widths(nums):
    MOD = 10**9 + 7
    
    # Sort the array to easily identify min/max contributions
    nums.sort()
    
    # Initialize result and power of 2
    result = 0
    power_of_two = 1
    
    # Process each element and its contribution
    for index, value in enumerate(nums):
        # For element at index i:
        # - As maximum: contributes +value * 2^i times
        # - As minimum: contributes -value * 2^(n-i-1) times
        # nums[-index-1] gives the element from the end (symmetric position)
        contribution = (value - nums[-index - 1]) * power_of_two
        result = (result + contribution) % MOD
        
        # Update power of 2 for next iteration (2^(i+1))
        power_of_two = (power_of_two * 2) % MOD
    
    return result
    # Time: O(n * log(n))
    # Space: O(1) or O(n)[considering sorting]


def main():
    result = sum_subseq_widths(nums = [2,1,3])
    print(result) # 6

    result = sum_subseq_widths(nums = [2])
    print(result) # 0

if __name__ == "__main__":
    main()

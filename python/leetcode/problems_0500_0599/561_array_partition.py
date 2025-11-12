# --------------------
# 561. Array Partition
# --------------------

# Problem: https://leetcode.com/problems/array-partition
#
# Given an integer array nums of 2n integers, group these integers into n pairs
# (a₁, b₁), (a₂, b₂), ..., (aₙ, bₙ) such that the sum of min(aᵢ, bᵢ) for all i is
# maximized. Return the maximized sum.
# 
# Example 1:
# 
# Input: nums = [1,4,3,2]
# Output: 4
# 
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
# 
# Example 2:
# 
# Input: nums = [6,2,6,5,1,2]
# Output: 9
# 
# Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2,
# 5) + min(6, 6) = 1 + 2 + 6 = 9.
# 
# 
# Constraints:
#         1 <= n <= 10⁴
#         nums.length == 2 * n
#         -10⁴ <= nums[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/561
# Credit: AlgoMonster
def array_pair_sum(nums):
    nums.sort()
    
    # Sum every alternate element starting from index 0 (elements at even indices)
    # nums[::2] creates a slice with step 2, giving us elements at indices 0, 2, 4, ...
    return sum(nums[::2])
    # Time: O(n * log(n))
    # Space: O(log(n))


def main():
    result = array_pair_sum(nums = [1,4,3,2])
    print(result) # 4

    result = array_pair_sum(nums = [6,2,6,5,1,2])
    print(result) # 9

if __name__ == "__main__":
    main()

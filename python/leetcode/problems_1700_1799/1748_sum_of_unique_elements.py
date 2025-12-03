# ----------------------------
# 1748. Sum of Unique Elements
# ----------------------------

# Problem: https://leetcode.com/problems/sum-of-unique-elements
#
# You are given an integer array nums. The unique elements of an array are the
# elements that appear exactly once in the array.
# 
# Return the sum of all the unique elements of nums.
# 
# Example 1:
# 
# Input: nums = [1,2,3,2]
# Output: 4
# 
# Explanation: The unique elements are [1,3], and the sum is 4.
# 
# Example 2:
# 
# Input: nums = [1,1,1,1,1]
# Output: 0
# 
# Explanation: There are no unique elements, and the sum is 0.
# 
# Example 3:
# 
# Input: nums = [1,2,3,4,5]
# Output: 15
# 
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
# 
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 100


# Solution: https://algo.monster/liteproblems/1748
# Credit: AlgoMonster
def sum_of_unique(nums):
    from collections import Counter

    # Count the frequency of each number in the array
    frequency_map = Counter(nums)
    
    # Sum up only the numbers that appear exactly once
    unique_sum = sum(num for num, count in frequency_map.items() if count == 1)
    
    return unique_sum
    # Time: O(n)
    # Space: O(n)


def main():
    result = sum_of_unique(nums = [1,2,3,2])
    print(result) # 4

    result = sum_of_unique(nums = [1,1,1,1,1])
    print(result) # 0

    result = sum_of_unique(nums = [1,2,3,4,5])
    print(result) # 15

if __name__ == "__main__":
    main()

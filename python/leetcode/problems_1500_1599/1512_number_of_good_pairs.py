# --------------------------
# 1512. Number of Good Pairs
# --------------------------

# Problem: https://leetcode.com/problems/number-of-good-pairs
#
# Given an array of integers nums, return the number of good pairs.
# 
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# 
# Example 1:
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# 
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# 
# Example 2:
# 
# Input: nums = [1,1,1,1]
# Output: 6
# 
# Explanation: Each pair in the array are good.
# 
# Example 3:
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# Constraints:
#         1 <= nums.length <= 100
#         1 <= nums[i] <= 100


# Solution: https://youtu.be/BqhDFUo1rjs
# Credit: Navdeep Singh founder of NeetCode
def num_identical_pairs(nums):
    res = 0
    count = {}
    for n in nums:
        if n in count:
            res += count[n]
            count[n] += 1
        else:
            count[n] = 1
    return res


def main():
    result = num_identical_pairs([1,2,3,1,1,3])
    print(result) # 4

    result = num_identical_pairs([1,1,1,1])
    print(result) # 6

    result = num_identical_pairs([1,2,3])
    print(result) # 0

if __name__ == "__main__":
    main()

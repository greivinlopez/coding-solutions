# ------------------------
# 229. Majority Element II
# ------------------------

# Problem: https://leetcode.com/problems/majority-element-ii
#
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# 
# Example 1:
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# Input: nums = [1]
# Output: [1]
# 
# Example 3:
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# Constraints:
#         1 <= nums.length <= 5 * 10^4
#         -10^9 <= nums[i] <= 10^9
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?

from collections import defaultdict

# Solution: https://youtu.be/Eua-UrQ_ANo
# Credit: Navdeep Singh founder of NeetCode
def majority_element(nums):
    count = defaultdict(int)
    
    for n in nums:
        count[n] += 1
    
        if len(count) <= 2:
            continue
        new_count = defaultdict(int)
        for n, c in count.items():
            if c > 1:
                new_count[n] = c - 1
        count = new_count
    
    res = []
    for n in count:
        if nums.count(n) > len(nums) // 3:
            res.append(n)
    return res
    # Time: O(n²)
    # Space: O(n)


def main():
    result = majority_element([3,2,3])
    print(result) # [3]

    result = majority_element([1])
    print(result) # [1]

    result = majority_element([1,2])
    print(result) # [1,2]

if __name__ == "__main__":
    main()

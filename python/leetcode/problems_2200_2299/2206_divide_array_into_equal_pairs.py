# -----------------------------------
# 2206. Divide Array Into Equal Pairs
# -----------------------------------

# Problem: https://leetcode.com/problems/divide-array-into-equal-pairs
#
# You are given an integer array nums consisting of 2 * n integers.
# 
# You need to divide nums into n pairs such that:
#         
#   * Each element belongs to exactly one pair.
#   * The elements present in a pair are equal.
# 
# Return true if nums can be divided into n pairs, otherwise return false.
# 
# Example 1:
# 
# Input: nums = [3,2,3,2,2,2]
# Output: true
# 
# Explanation:
# There are 6 elements in nums, so they should be divided into 6 / 2 = 3 pairs.
# If nums is divided into the pairs (2, 2), (3, 3), and (2, 2), it will satisfy
# all the conditions.
# 
# Example 2:
# 
# Input: nums = [1,2,3,4]
# Output: false
# 
# Explanation:
# There is no way to divide nums into 4 / 2 = 2 pairs such that the pairs satisfy
# every condition.
# 
# 
# Constraints:
#         nums.length == 2 * n
#         1 <= n <= 500
#         1 <= nums[i] <= 500


# Solution: https://youtu.be/vxcpdClAktE
# Credit: Navdeep Singh founder of NeetCode
def divide_array(nums):
    count = {}
    for n in nums:
        if n not in count:
            count[n] = 0
        count[n] += 1
    for n, cnt in count.items():
        if cnt % 2:
            return False
    return True
    # Time: O(n)
    # Space: O(1)

def divide_array_alt(nums):
    # Alternative solution
    odd_set = set()
    for n in nums:
        if n not in odd_set:
            odd_set.add(n)
        else:
            odd_set.remove(n)
    return len(odd_set) == 0
    # Time: O(n)
    # Space: O(1)


def main():
    result = divide_array(nums = [3,2,3,2,2,2])
    print(result) # True

    result = divide_array(nums = [1,2,3,4])
    print(result) # False

if __name__ == "__main__":
    main()

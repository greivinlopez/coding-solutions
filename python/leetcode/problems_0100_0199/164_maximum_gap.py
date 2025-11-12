# ----------------
# 164. Maximum Gap
# ----------------

# Problem: https://leetcode.com/problems/maximum-gap
#
# Given an integer array nums, return the maximum difference between two
# successive elements in its sorted form. If the array contains less than two
# elements, return 0.
# 
# You must write an algorithm that runs in linear time and uses linear extra
# space.
# 
# Example 1:
# 
# Input: nums = [3,6,9,1]
# Output: 3
# 
# Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9)
# has the maximum difference 3.
# 
# Example 2:
# 
# Input: nums = [10]
# Output: 0
# 
# Explanation: The array contains less than 2 elements, therefore return 0.
# 
# 
# Constraints:
#         1 <= nums.length <= 10⁵
#         0 <= nums[i] <= 10⁹

from collections import defaultdict

# Solution: https://leetcode.com/problems/maximum-gap/solutions/4980638/using-bucket-sort-python
# Credit: Pragya Maheshwari -> https://leetcode.com/u/pragya_2305/
def maximum_gap(nums):
    n = len(nums)
    lo,hi = min(nums),max(nums)
    B = defaultdict(list)
    for num in nums:
        if num == hi:
            ind = n-1
        else:
            ind = (abs(num-lo)*(n-1))//(hi-lo)
        B[ind].append(num)

    buckets = []
    for i in range(n):
        if B[i]:
            buckets.append((min(B[i]),max(B[i])))

    ans = 0
    for i in range(1,len(buckets)):
        ans = max(ans,abs(buckets[i-1][-1]-buckets[i][0]))
    return ans
    # Time: O(n)
    # Space: O(n)


def main():
    result = maximum_gap([3,6,9,1])
    print(result) # 3

    result = maximum_gap([10])
    print(result) # 0

if __name__ == "__main__":
    main()

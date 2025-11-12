# -------------------------------
# 349. Intersection Of Two Arrays
# -------------------------------

# Problem: https://leetcode.com/problems/intersection-of-two-arrays/
# 
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must be unique and you may return 
# the result in any order.
# 
#  
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
# 
# 
# Constraints:
# 
# 	1 <= nums1.length, nums2.length <= 1000
# 	0 <= nums1[i], nums2[i] <= 1000


# Solution: https://youtu.be/fwUTXaMom6U
# Credit: Navdeep Singh founder of NeetCode
def intersection(nums1, nums2):
    seen = set(nums1)

    res = []
    for n in nums2:
        if n in seen:
            res.append(n)
            seen.remove(n)
    return res


def main():
    result = intersection(nums1 = [1,2,2,1], nums2 = [2,2])
    print(result) # [2]

    result = intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    print(result) # [9,4]

if __name__ == "__main__":
    main()

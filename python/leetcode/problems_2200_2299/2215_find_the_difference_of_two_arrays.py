# --------------------------------------
# 2215. Find The Difference Of Two Arrays
# --------------------------------------

# Problem: https://leetcode.com/problems/find-the-difference-of-two-arrays
#
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size
# 2 where:
#
#   answer[0] is a list of all distinct integers in nums1 which are not
#   present in nums2.
# 
#   answer[1] is a list of all distinct integers in nums2 which are not
#   present in nums1.
# 
# Note that the integers in the lists may be returned in any order.
# 
# Example 1:
# 
# Input: nums1 = [1,2,3], nums2 = [2,4,6]
# Output: [[1,3],[4,6]]
# Explanation:
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and
# nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and
# nums2[2] = 6 are not present in nums1. Therefore, answer[1] = [4,6].
# 
# Example 2:
# 
# Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
# Output: [[3],[]]
# Explanation:
# For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] ==
# nums1[3], their value is only included once and answer[0] = [3].
# Every integer in nums2 is present in nums1. Therefore, answer[1] = [].
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 1000
#         -1000 <= nums1[i], nums2[i] <= 1000


# Solution: https://youtu.be/a4wqKR-znBE
# Credit: Navdeep Singh founder of NeetCode
def find_difference(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    table = {}
    for _, val in enumerate(nums2):
        table[val] = 1

    unik1 = []
    unik2 = []
    for i in nums1:
        if i in table:
            table[i] += 1
        else:
            unik1.append(i)
    
    for key, val in table.items():
        if val == 1:
            unik2.append(key)
    return [unik1, unik2]
    # Time: O(m + n)
    # Space: O(m + n)

def find_difference_alt(nums1, nums2):
    nums1_set = set(nums1)
    nums2_set = set(nums2)

    lst1 = [num for num in nums1_set if num not in nums2_set]
    lst2 = [num for num in nums2_set if num not in nums1_set]

    return [lst1, lst2]
    # Time: O(m + n) we check each element of nums1Set and nums2Set
    # Space: O(m + n) where m and n are length sets in worst case.


def main():
    result = find_difference(nums1 = [1,2,3], nums2 = [2,4,6])
    print(result) # [[1,3],[4,6]]

    result = find_difference(nums1 = [1,2,3,3], nums2 = [1,1,2,2])
    print(result) # [[3],[]]

if __name__ == "__main__":
    main()

# --------------------------
# 2540. Minimum Common Value
# --------------------------

# Problem: https://leetcode.com/problems/minimum-common-value
#
# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return
# the minimum integer common to both arrays. If there is no common integer amongst
# nums1 and nums2, return -1.
# 
# Note that an integer is said to be common to nums1 and nums2 if both arrays have
# at least one occurrence of that integer.
# 
# Example 1:
# 
# Input: nums1 = [1,2,3], nums2 = [2,4]
# Output: 2
# 
# Explanation: The smallest element common to both arrays is 2, so we return 2.
# 
# Example 2:
# 
# Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
# Output: 2
# 
# Explanation: There are two common elements in the array 2 and 3 out of which 2
# is the smallest, so 2 is returned.
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 105
#         1 <= nums1[i], nums2[j] <= 109
#         Both nums1 and nums2 are sorted in non-decreasing order.


# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def get_common(nums1, nums2):
    first = 0
    second = 0

    # Traverse through both arrays with two pointers
    # Increment the pointer with a smaller value at that index
    # Return the first common element found
    while first < len(nums1) and second < len(nums2):
        if nums1[first] < nums2[second]:
            first += 1
        elif nums1[first] > nums2[second]:
            second += 1
        else:
            return nums1[first]

    # Return -1 if there are no common elements
    return -1
    # Time: O(n)
    # Space: O(1)


def main():
    result = get_common(nums1 = [1,2,3], nums2 = [2,4])
    print(result) # 2

    result = get_common(nums1 = [1,2,3,6], nums2 = [2,3,4,5])
    print(result) # 2

if __name__ == "__main__":
    main()

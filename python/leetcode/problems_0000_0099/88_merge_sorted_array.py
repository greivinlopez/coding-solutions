# -----------------------
# 88. Merge Sorted Array
# -----------------------

# Problem: https://leetcode.com/problems/merge-sorted-array/
# 
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 
# respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function, but instead be 
# stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the 
# last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Solution: https://youtu.be/P1Ic85RarKY
# Credit: Navdeep Singh founder of NeetCode
def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

# Solution: https://youtu.be/0-KuWOcHZuk
# Credit: Greg Hogg
def merge_alt(nums1, m, nums2, n):
    # Time: O(n + m)
    # Space: O(1)
    x, y = m-1, n-1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1

def main():
    nums1 = [1,2,3,0,0,0]
    merge(nums1, m = 3, nums2 = [2,5,6], n = 3)
    print(nums1) # [1,2,2,3,5,6]

    nums1 = [1]
    merge(nums1, m = 1, nums2 = [], n = 0)
    print(nums1) # [1]

    nums1 = [0]
    merge(nums1, m = 0, nums2 = [1], n = 1)
    print(nums1) # [1]

if __name__ == "__main__":
    main()
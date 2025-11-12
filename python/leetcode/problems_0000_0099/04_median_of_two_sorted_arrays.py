# ------------------------------
# 4. Median of Two Sorted Arrays
# ------------------------------

# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
# median of the two sorted arrays.
# 
# The overall run time complexity should be O(log(m+n)).
# 
# Example 1:
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# 
# Explanation: merged array = [1,2,3] and median is 2.
# 
# Example 2:
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# 
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# Constraints:
#         nums1.length == m
#         nums2.length == n
#         0 <= m <= 1000
#         0 <= n <= 1000
#         1 <= m + n <= 2000
#         -10⁶ <= nums1[i], nums2[i] <= 10⁶


# Solution: https://youtu.be/q6IEA26hvXc
# Credit: Navdeep Singh founder of NeetCode 
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2  # A
        j = half - i - 2  # B

        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
    # Time: O(log(min(n, m)))
    # Space: O(1)

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def find_median_sorted_arrays_alt(nums1, nums2):
    m, n = len(nums1), len(nums2)
    p1, p2 = 0, 0
    
    def get_min():
        nonlocal p1, p2
        
        if p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
        elif p2 == n:
            ans = nums1[p1]
            p1 += 1
        else:
            ans = nums2[p2]
            p2 += 1
        
        return ans
    
    if (m+n) % 2 == 0:
        for _ in range((m+n)//2-1):
            _ = get_min()
        return (get_min() + get_min()) / 2
    else:
        for _ in range((m+n)//2):
            _ = get_min()
        return get_min()
    # Time: O(n + m)
    # Space: O(1)


def main():
    result = find_median_sorted_arrays([1,3], [2]) # 2.000
    print(result)
    result = find_median_sorted_arrays([1,2], [3,4]) # 2.500
    print(result)

if __name__ == "__main__":
    main()
# --------------------------
# 321. Create Maximum Number
# --------------------------

# Problem: https://leetcode.com/problems/create-maximum-number
#
# You are given two integer arrays nums1 and nums2 of lengths m and n
# respectively. nums1 and nums2 represent the digits of two numbers. You are also
# given an integer k.
# 
# Create the maximum number of length k <= m + n from digits of the two numbers.
# The relative order of the digits from the same array must be preserved.
# 
# Return an array of the k digits representing the answer.
# 
# Example 1:
# 
# Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
# Output: [9,8,6,5,3]
# 
# Example 2:
# 
# Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
# Output: [6,7,6,0,4]
# 
# Example 3:
# 
# Input: nums1 = [3,9], nums2 = [8,9], k = 3
# Output: [9,8,9]
# 
# 
# Constraints:
#         m == nums1.length
#         n == nums2.length
#         1 <= m, n <= 500
#         0 <= nums1[i], nums2[i] <= 9
#         1 <= k <= m + n
#         nums1 and nums2 do not have leading zeros.


# Solution: https://leetcode.com/problems/create-maximum-number/solutions/1027086/python-solution-greedy-search-dynamic-programming
# Credit: Jie Min -> https://leetcode.com/u/jmin3/
def max_number(nums1, nums2, k):
    def merge(n1, n2):
        res = []
        while (n1 or n2) :
            if n1>n2:
                res.append(n1[0])
                n1 = n1[1:]
            else:
                res.append(n2[0])
                n2 = n2[1:]
        return res
    
    def findmax(nums, length):
        l = []
        maxpop = len(nums)-length
        for i in range(len(nums)):
            while maxpop>0 and len(l) and nums[i]>l[-1]:
                l.pop()
                maxpop -= 1
            l.append(nums[i])
        return l[:length]
    
    n1 = len(nums1)
    n2 = len(nums2)
    res = [0]*k
    for i in range(k+1):
        j = k-i
        if i>n1 or j>n2:    continue
        l1 = findmax(nums1, i)
        l2 = findmax(nums2, j)
        res = max(res, merge(l1,l2))
    return res
    # Time: O(k² × (n1 + n2)²)
    # Space: O(k²)


def main():
    result = max_number(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5)
    print(result) # [9,8,6,5,3]

    result = max_number(nums1 = [6,7], nums2 = [6,0,4], k = 5)
    print(result) # [6,7,6,0,4]

    result = max_number(nums1 = [3,9], nums2 = [8,9], k = 3)
    print(result) # [9,8,9]

if __name__ == "__main__":
    main()

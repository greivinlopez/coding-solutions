# ---------------------------
# 496. Next Greater Element I
# ---------------------------

# Problem: https://leetcode.com/problems/next-greater-element-i/
# 
# The next greater element of some element x in an array is the first greater 
# element that is to the right of x in the same array.
# 
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where 
# nums1 is a subset of nums2.
# 
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] 
# and determine the next greater element of nums2[j] in nums2. If there is no 
# next greater element, then the answer for this query is -1.
# 
# Return an array ans of length nums1.length such that ans[i] is the next 
# greater element as described above.
# 
#  
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
# 
# 
# Constraints:
# 
# 	1 <= nums1.length <= nums2.length <= 1000
# 	0 <= nums1[i], nums2[i] <= 10^4
# 	All integers in nums1 and nums2 are unique.
# 	All the integers of nums1 also appear in nums2.
#  
# Follow up: Could you find an O(nums1.length + nums2.length) solution?


# Solution: https://youtu.be/68a1Dc_qVq4
# Credit: Navdeep Singh founder of NeetCode
def next_greater_element(nums1, nums2):
    nums1Idx = { n:i for i, n in enumerate(nums1) }
    res = [-1] * len(nums1)

    stack = []
    for i in range(len(nums2)):
        cur = nums2[i]

        # while stack exists and current is greater than the top of the stack
        while stack and cur > stack[-1]:
            val = stack.pop() # take top val
            idx = nums1Idx[val]
            res[idx] = cur

        if cur in nums1Idx:
            stack.append(cur)
    
    return res
    # Time: O(n + m)

def next_greater_element_alt(nums1, nums2):
    nums1Idx = { n:i for i, n in enumerate(nums1) }
    res = [-1] * len(nums1)
    
    for i in range(len(nums2)):
        if nums2[i] not in nums1Idx:
            continue
        for j in range(i + 1, len(nums2)):
            if nums2[j] > nums2[i]:
                idx = nums1Idx[nums2[i]]
                res[idx] = nums2[j]
                break
    
    return res
    # Time: O(n * m)

def main():
    result = next_greater_element(nums1 = [4,1,2], nums2 = [1,3,4,2])
    print(result) # [-1,3,-1]

    result = next_greater_element(nums1 = [2,4], nums2 = [1,2,3,4])
    print(result) # [3,-1]

if __name__ == "__main__":
    main()

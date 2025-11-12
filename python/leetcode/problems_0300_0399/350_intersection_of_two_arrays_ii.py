# ----------------------------------
# 350. Intersection Of Two Arrays II
# ----------------------------------

# Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 
# Given two integer arrays nums1 and nums2, return an array of their 
# intersection. Each element in the result must appear as many times as it 
# shows in both arrays and you may return the result in any order.
# 
#  
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
# 
#  
# Constraints:
# 
# 	1 <= nums1.length, nums2.length <= 1000
# 	0 <= nums1[i], nums2[i] <= 1000
# 
# 
# Follow up:
# 
# 	What if the given array is already sorted? How would you optimize your algorithm?
# 	What if nums1's size is small compared to nums2's size? Which algorithm is better?
# 	What if elements of nums2 are stored on disk, and the memory is limited such that 
#   you cannot load all elements into the memory at once?


# Solution: No video found
# Credit: Navdeep Singh founder of NeetCode
from collections import Counter, defaultdict
def intersect(nums1, nums2):
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)

    # Using defaultdict to handle missing keys more efficiently
    counter1 = defaultdict(int, counter1)
    counter2 = defaultdict(int, counter2)

    intersection = []

    for num, freq in counter1.items():
        min_freq = min(freq, counter2[num])
        if min_freq > 0:
            intersection.extend([num] * min_freq)

    return intersection


def main():
    result = intersect(nums1 = [1,2,2,1], nums2 = [2,2])
    print(result) # [2, 2]

    result = intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])
    print(result) # [4, 9]

if __name__ == "__main__":
    main()

# ---------------------------
# 1537. Get the Maximum Score
# ---------------------------

# Problem: https://leetcode.com/problems/get-the-maximum-score
#
# You are given two sorted arrays of distinct integers nums1 and nums2.
# 
# A valid path is defined as follows:
#         
#   * Choose array nums1 or nums2 to traverse (from index-0).
#   * Traverse the current array from left to right.
#   * If you are reading any value that is present in nums1 and nums2 you are
#     allowed to change your path to the other array. (Only one repeated value is
#     considered in the valid path).
# 
# The score is defined as the sum of unique values in a valid path.
# 
# Return the maximum score you can obtain of all possible valid paths. Since the
# answer may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# https://assets.leetcode.com/uploads/2020/07/16/sample_1_1893.png
# 
# Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
# Output: 30
# 
# Explanation: Valid paths:
# [2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
# [4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
# The maximum is obtained with the path in green [2,4,6,8,10].
# 
# Example 2:
# 
# Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
# Output: 109
# 
# Explanation: Maximum sum is obtained with the path [1,3,5,100].
# 
# Example 3:
# 
# Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
# Output: 40
# 
# Explanation: There are no common elements between nums1 and nums2.
# Maximum sum is obtained with the path [6,7,8,9,10].
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 10⁵
#         1 <= nums1[i], nums2[i] <= 10⁷
#         nums1 and nums2 are strictly increasing.


# Solution: https://algo.monster/liteproblems/1537
# Credit: AlgoMonster
def max_sum(nums1, nums2):
    MOD = 10**9 + 7
    len1, len2 = len(nums1), len(nums2)
    
    # Two pointers for traversing both arrays
    pointer1 = pointer2 = 0
    
    # Running sums for paths through nums1 and nums2 respectively
    sum_path1 = sum_path2 = 0
    
    # Process both arrays using two pointers
    while pointer1 < len1 or pointer2 < len2:
        # If we've exhausted nums1, add remaining elements from nums2
        if pointer1 == len1:
            sum_path2 += nums2[pointer2]
            pointer2 += 1
        # If we've exhausted nums2, add remaining elements from nums1
        elif pointer2 == len2:
            sum_path1 += nums1[pointer1]
            pointer1 += 1
        # If current element in nums1 is smaller, add it to path1
        elif nums1[pointer1] < nums2[pointer2]:
            sum_path1 += nums1[pointer1]
            pointer1 += 1
        # If current element in nums2 is smaller, add it to path2
        elif nums1[pointer1] > nums2[pointer2]:
            sum_path2 += nums2[pointer2]
            pointer2 += 1
        # If elements are equal (intersection point)
        else:
            # At intersection, take the maximum sum so far and add current element
            # Both paths now have the same sum after this intersection
            sum_path1 = sum_path2 = max(sum_path1, sum_path2) + nums1[pointer1]
            pointer1 += 1
            pointer2 += 1
    
    # Return the maximum of the two path sums, modulo MOD
    return max(sum_path1, sum_path2) % MOD
    # Time: O(m + n)
    # Space: O(1)


def main():
    result = max_sum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9])
    print(result) # 30

    result = max_sum(nums1 = [1,3,5,7,9], nums2 = [3,5,100])
    print(result) # 109

    result = max_sum(nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10])
    print(result) # 40

if __name__ == "__main__":
    main()

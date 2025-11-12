# ------------------------------------
# 373. Find K Pairs with Smallest Sums
# ------------------------------------

# Problem: https://leetcode.com/problems/find-k-pairs-with-smallest-sums
#
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order
# and an integer k.
# 
# Define a pair (u, v) which consists of one element from the first array and one
# element from the second array.
# 
# Return the k pairs (u₁, v₁), (u₂, v₂), ..., (uₖ, vₖ) with the smallest sums.
# 
# Example 1:
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# 
# Explanation: The first 3 pairs are returned from the sequence:
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# Example 2:
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# 
# Explanation: The first 2 pairs are returned from the sequence:
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# Constraints:
#         1 <= nums1.length, nums2.length <= 10⁵
#         -10⁹ <= nums1[i], nums2[i] <= 10⁹
#         nums1 and nums2 both are sorted in non-decreasing order.
#         1 <= k <= 10⁴
#         k <= nums1.length * nums2.length

import heapq

# Solution: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/solutions/3686980/from-dumb-to-pro-with-just-one-visit-my-promise-to-you-with-efficient-selection-of-k-smallest-pair
# Credit: Amit Roy -> https://leetcode.com/u/curio_sity/
def k_smallest_pairs(nums1, nums2, k):
    resV = []
    pq = []

    for x in nums1:
        heapq.heappush(pq, [x + nums2[0], 0])

    while k > 0 and pq:
        pair = heapq.heappop(pq)
        s, pos = pair[0], pair[1]

        resV.append([s - nums2[pos], nums2[pos]])

        if pos + 1 < len(nums2):
            heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])

        k -= 1

    return resV


def main():
    result = k_smallest_pairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3)
    print(result) # [[1,2],[1,4],[1,6]]

    result = k_smallest_pairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2)
    print(result) # [[1,1],[1,1]]

if __name__ == "__main__":
    main()

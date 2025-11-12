# ----------------------------------------
# 1471. The k Strongest Values in an Array
# ----------------------------------------

# Problem: https://leetcode.com/problems/the-k-strongest-values-in-an-array
#
# Given an array of integers arr and an integer k.
# 
# A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| >
# |arr[j] - m| where m is the centre of the array.
# If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j]
# if arr[i] > arr[j].
# 
# Return a list of the strongest k values in the array. return the answer in any
# arbitrary order.
# 
# The centre is the middle value in an ordered integer list. More formally, if the
# length of the list is n, the centre is the element in position ((n - 1) / 2) in
# the sorted list (0-indexed).
#         
#   * For arr = [6, -3, 7, 2, 11], n = 5 and the centre is obtained by sorting the 
#     array arr = [-3, 2, 6, 7, 11] and the centre is arr[m] where m = ((5 - 1) / 2) = 2. 
#     The centre is 6.
#   * For arr = [-7, 22, 17, 3], n = 4 and the centre is obtained by sorting the 
#     array arr = [-7, 3, 17, 22] and the centre is arr[m] where m = ((4 - 1) / 2) = 1. 
#     The centre is 3.
# 
# Example 1:
# 
# Input: arr = [1,2,3,4,5], k = 2
# Output: [5,1]
# 
# Explanation: Centre is 3, the elements of the array sorted by the strongest are
# [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted
# answer.
# Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5
# > 1.
# 
# Example 2:
# 
# Input: arr = [1,1,3,5,5], k = 2
# Output: [5,5]
# 
# Explanation: Centre is 3, the elements of the array sorted by the strongest are
# [5,5,1,1,3]. The strongest 2 elements are [5, 5].
# 
# Example 3:
# 
# Input: arr = [6,7,11,7,6,8], k = 5
# Output: [11,8,6,6,7]
# 
# Explanation: Centre is 7, the elements of the array sorted by the strongest are
# [11,8,6,6,7,7].
# Any permutation of [11,8,6,6,7] is accepted.
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁵
#         -10⁵ <= arr[i] <= 10⁵
#         1 <= k <= arr.length


# Solution: https://algo.monster/liteproblems/1471
# Credit: AlgoMonster
def get_strongest(arr, k):
    # Sort the array to find the median
    arr.sort()
    
    # Calculate the median index using integer division
    # For odd length: (n-1)/2, for even length: (n-1)/2 (rounds down)
    median_index = (len(arr) - 1) // 2
    median_value = arr[median_index]
    
    # Sort array by "strongest" criteria:
    # 1. Primary: Larger absolute difference from median (descending)
    # 2. Secondary: Larger value (descending) when differences are equal
    arr.sort(key=lambda element: (-abs(element - median_value), -element))
    
    # Return the k strongest elements
    return arr[:k]
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = get_strongest(arr = [1,2,3,4,5], k = 2)
    print(result) # [5, 1]

    result = get_strongest(arr = [1,1,3,5,5], k = 2)
    print(result) # [5, 5]

    result = get_strongest(arr = [6,7,11,7,6,8], k = 5)
    print(result) # [11, 8, 6, 6, 7]

if __name__ == "__main__":
    main()

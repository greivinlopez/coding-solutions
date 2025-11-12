# ---------------------------------
# 1200. Minimum Absolute Difference
# ---------------------------------

# Problem: https://leetcode.com/problems/minimum-absolute-difference
#
# Given an array of distinct integers arr, find all pairs of elements with the
# minimum absolute difference of any two elements.
# 
# Return a list of pairs in ascending order(with respect to pairs), each pair [a,
# b] follows
#         
#       a, b are from arr
#       a < b
#       b - a equals to the minimum absolute difference of any two elements in arr
# 
# Example 1:
# 
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]
# 
# Explanation: The minimum absolute difference is 1. List all pairs with
# difference equal to 1 in ascending order.
# 
# Example 2:
# 
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]
# 
# Example 3:
# 
# Input: arr = [3,8,-10,23,19,-4,-14,27]
# Output: [[-14,-10],[19,23],[23,27]]
# 
# 
# Constraints:
#         2 <= arr.length <= 10⁵
#         -10⁶ <= arr[i] <= 10⁶


# Solution: https://algo.monster/liteproblems/1200
# Credit: AlgoMonster
def minimum_abs_difference(arr):
    # Sort the array to find adjacent pairs with minimum difference
    arr.sort()
    
    # Find the minimum absolute difference between consecutive elements
    min_diff = float('inf')
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i - 1]
        min_diff = min(min_diff, diff)
    
    # Collect all pairs that have the minimum absolute difference
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == min_diff:
            result.append([arr[i - 1], arr[i]])
    
    return result
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = minimum_abs_difference(arr = [4,2,1,3])
    print(result) # [[1, 2], [2, 3], [3, 4]]

    result = minimum_abs_difference(arr = [1,3,6,10,15])
    print(result) # [[1, 3]]

    result = minimum_abs_difference(arr = [3,8,-10,23,19,-4,-14,27])
    print(result) # [[-14, -10], [19, 23], [23, 27]]

if __name__ == "__main__":
    main()

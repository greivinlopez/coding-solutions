# --------------------------------
# 1331. Rank Transform of an Array
# --------------------------------

# Problem: https://leetcode.com/problems/rank-transform-of-an-array
#
# Given an array of integers arr, replace each element with its rank.
# 
# The rank represents how large the element is. The rank has the following rules:
#         
#   * Rank is an integer starting from 1.
#   * The larger the element, the larger the rank. If two elements are equal,
#     their rank must be the same.
#   * Rank should be as small as possible.
# 
# Example 1:
# 
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# 
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second
# smallest. 30 is the third smallest.
# 
# Example 2:
# 
# Input: arr = [100,100,100]
# Output: [1,1,1]
# 
# Explanation: Same elements share the same rank.
# 
# Example 3:
# 
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]
# 
# 
# Constraints:
#         0 <= arr.length <= 10⁵
#         -10⁹ <= arr[i] <= 10⁹

from bisect import bisect_right

# Solution: https://algo.monster/liteproblems/1331
# Credit: AlgoMonster
def array_rank_transform_a(arr):
    # Create a sorted list of unique elements from the array
    # This represents all distinct values in ascending order
    unique_sorted = sorted(set(arr))
    
    # For each element in the original array, find its rank
    # bisect_right returns the insertion position, which equals the rank
    # since we're using 1-based ranking (position 0 means rank 1)
    return [bisect_right(unique_sorted, x) for x in arr]
    # Time: O(n * log n)
    # Space: O(n)

# Alternative Solution: https://leetcode.com/problems/rank-transform-of-an-array/solutions/5858548/python-sorting-hashing-by-khosiyat-jwkh
# Credit: Khosiyat Sabir -> https://leetcode.com/u/Khosiyat/
def array_rank_transform(arr):
    # Create a sorted list of the unique elements in arr
    sorted_unique = sorted(set(arr))
    
    # Create a dictionary mapping each element to its rank
    rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
    
    # Replace each element in the original array with its rank
    return [rank_dict[num] for num in arr]
    # Time: O(n * log n)
    # Space: O(n)


def main():
    result = array_rank_transform(arr = [40,10,20,30])
    print(result) # [4, 1, 2, 3]

    result = array_rank_transform(arr = [100,100,100])
    print(result) # [1, 1, 1]

    result = array_rank_transform(arr = [37,12,28,9,100,56,80,5,12])
    print(result) # [5, 3, 4, 2, 8, 6, 7, 1, 3]

if __name__ == "__main__":
    main()

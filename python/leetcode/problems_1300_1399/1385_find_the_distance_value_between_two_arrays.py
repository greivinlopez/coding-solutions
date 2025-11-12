# ------------------------------------------------
# 1385. Find the Distance Value Between Two Arrays
# ------------------------------------------------

# Problem: https://leetcode.com/problems/find-the-distance-value-between-two-arrays
#
# Given two integer arrays arr1 and arr2, and the integer d, return the distance
# value between the two arrays.
# 
# The distance value is defined as the number of elements arr1[i] such that there
# is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
# 
# Example 1:
# 
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# 
# Explanation:
# For arr1[0]=4 we have:
# |4-10|=6 > d=2
# |4-9|=5 > d=2
# |4-1|=3 > d=2
# |4-8|=4 > d=2
# For arr1[1]=5 we have:
# |5-10|=5 > d=2
# |5-9|=4 > d=2
# |5-1|=4 > d=2
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2
# 
# Example 2:
# 
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2
# 
# Example 3:
# 
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1
# 
# 
# Constraints:
#         1 <= arr1.length, arr2.length <= 500
#         -1000 <= arr1[i], arr2[j] <= 1000
#         0 <= d <= 100

from bisect import bisect_left

# Solution: https://algo.monster/liteproblems/1385
# Credit: AlgoMonster
def find_the_distance_value(arr1, arr2, d):
    # Sort arr2 to enable binary search
    arr2.sort()
    
    # Initialize counter for valid elements
    distance_value_count = 0
    
    # Check each element in arr1
    for num in arr1:
        # Find the leftmost position where (num - d) could be inserted in arr2
        # This gives us the index of the smallest element >= (num - d)
        left_bound_index = bisect_left(arr2, num - d)
        
        # An element from arr1 is valid if:
        # 1. left_bound_index == len(arr2): all elements in arr2 are < (num - d)
        # 2. arr2[left_bound_index] > (num + d): the smallest element >= (num - d) is also > (num + d)
        # Both conditions mean no element in arr2 is within distance d from num
        is_valid = (left_bound_index == len(arr2) or arr2[left_bound_index] > num + d)
        distance_value_count += is_valid
    
    return distance_value_count
    # Time: O(n log n + m log n)
    # Space: O(log n)


def main():
    result = find_the_distance_value(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2)
    print(result) # 2

    result = find_the_distance_value(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3)
    print(result) # 2

    result = find_the_distance_value(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6)
    print(result) # 1

if __name__ == "__main__":
    main()

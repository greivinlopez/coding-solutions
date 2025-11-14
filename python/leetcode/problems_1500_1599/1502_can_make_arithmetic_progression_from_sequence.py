# ---------------------------------------------------
# 1502. Can Make Arithmetic Progression From Sequence
# ---------------------------------------------------

# Problem: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence
#
# A sequence of numbers is called an arithmetic progression if the difference
# between any two consecutive elements is the same.
# 
# Given an array of numbers arr, return true if the array can be rearranged to
# form an arithmetic progression. Otherwise, return false.
# 
# Example 1:
# 
# Input: arr = [3,5,1]
# Output: true
# 
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences
# 2 and -2 respectively, between each consecutive elements.
# 
# Example 2:
# 
# Input: arr = [1,2,4]
# Output: false
# 
# Explanation: There is no way to reorder the elements to obtain an arithmetic
# progression.
# 
# 
# Constraints:
#         2 <= arr.length <= 1000
#         -10⁶ <= arr[i] <= 10⁶


# Solution: https://algo.monster/liteproblems/1502
# Credit: AlgoMonster
def can_make_arithmetic_progression(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Calculate the common difference using first two elements
    common_difference = arr[1] - arr[0]
    
    # Check if all consecutive pairs have the same difference
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != common_difference:
            return False
    
    return True
    # Time: O(n * log n)
    # Space: O(log n)


# Alternative Solution: Python 3.10+
# Credit: AlgoMonster
def can_make_arithmetic_progression(arr):
    from itertools import pairwise

    # Sort the array in ascending order
    arr.sort()
    
    # Calculate the common difference using first two elements
    common_difference = arr[1] - arr[0]
    
    # Check if all consecutive pairs have the same difference
    # Using itertools.pairwise to iterate through consecutive pairs
    return all(second - first == common_difference 
                for first, second in pairwise(arr))
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = can_make_arithmetic_progression(arr = [3,5,1])
    print(result) # True

    result = can_make_arithmetic_progression(arr = [1,2,4])
    print(result) # False

if __name__ == "__main__":
    main()

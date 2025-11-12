# --------------------------------------------
# 1300. Sum of Mutated Array Closest to Target
# --------------------------------------------

# Problem: https://leetcode.com/problems/sum-of-mutated-array-closest-to-target
#
# Given an integer array arr and a target value target, return the integer value
# such that when we change all the integers larger than value in the given array
# to be equal to value, the sum of the array gets as close as possible (in
# absolute difference) to target.
# 
# In case of a tie, return the minimum such integer.
# 
# Notice that the answer is not neccesarilly a number from arr.
# 
# Example 1:
# 
# Input: arr = [4,9,3], target = 10
# Output: 3
# 
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the
# optimal answer.
# 
# Example 2:
# 
# Input: arr = [2,3,5], target = 10
# Output: 5
# 
# Example 3:
# 
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         1 <= arr[i], target <= 10⁵

from itertools import accumulate
from bisect import bisect_right

# Solution: https://algo.monster/liteproblems/1300
# Credit: AlgoMonster
def find_best_value(arr, target):
    # Sort the array for binary search and prefix sum calculation
    arr.sort()
    
    # Create prefix sum array with initial 0 for easier indexing
    # prefix_sums[i] represents sum of first i elements
    prefix_sums = list(accumulate(arr, initial=0))
    
    # Initialize variables to track the best value and minimum difference
    best_value = 0
    min_difference = float('inf')
    
    # Try all possible values from 0 to max element in array
    for candidate_value in range(max(arr) + 1):
        # Find the index where candidate_value would be inserted
        # This gives us the count of elements <= candidate_value
        index = bisect_right(arr, candidate_value)
        
        # Calculate the sum after replacing all elements > candidate_value
        # Sum = (sum of elements <= candidate_value) + (count of elements > candidate_value) * candidate_value
        current_sum = prefix_sums[index] + (len(arr) - index) * candidate_value
        
        # Calculate absolute difference from target
        current_difference = abs(current_sum - target)
        
        # Update best value if we found a smaller difference
        if current_difference < min_difference:
            min_difference = current_difference
            best_value = candidate_value
    
    return best_value
    # Time: O(n * log n + m * log n)
    # Space: O(n)
    # n = the length of the array arr
    # m = the maximum value in the array.


def main():
    result = find_best_value(arr = [4,9,3], target = 10)
    print(result) # 3

    result = find_best_value(arr = [2,3,5], target = 10)
    print(result) # 5

    result = find_best_value(arr = [60864,25176,27249,21296,20204], target = 56803)
    print(result) # 11361

if __name__ == "__main__":
    main()

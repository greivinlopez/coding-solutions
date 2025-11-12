# ---------------------------
# 923. 3Sum With Multiplicity
# ---------------------------

# Problem: https://leetcode.com/problems/3sum-with-multiplicity
#
# Given an integer array arr, and an integer target, return the number of tuples
# i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
# 
# As the answer can be very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# 
# Explanation:
# Enumerating by the values (arr[i], arr[j], arr[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# 
# Example 2:
# 
# Input: arr = [1,1,2,2,2,2], target = 5
# Output: 12
# 
# Explanation:
# arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
# 
# Example 3:
# 
# Input: arr = [2,1,3], target = 6
# Output: 1
# 
# Explanation: (1, 2, 3) occured one time in the array so we return 1.
# 
# 
# Constraints:
#         3 <= arr.length <= 3000
#         0 <= arr[i] <= 100
#         0 <= target <= 300

from collections import Counter

# Solution: https://algo.monster/liteproblems/923
# Credit: AlgoMonster
def three_sum_multi(arr, target):
    # Define modulo constant for large number handling
    MOD = 10**9 + 7
    
    # Count frequency of each element in the array
    frequency_map = Counter(arr)
    
    # Initialize result counter
    triplet_count = 0
    
    # Iterate through middle element position
    for middle_idx, middle_val in enumerate(arr):
        # Decrement count of middle element to avoid reusing it
        frequency_map[middle_val] -= 1
        
        # Check all elements before middle position as first element
        for left_val in arr[:middle_idx]:
            # Calculate required third element value
            required_third = target - left_val - middle_val
            
            # Add count of valid third elements (must be after middle_idx)
            triplet_count = (triplet_count + frequency_map[required_third]) % MOD
            
    return triplet_count
    # Time: O(n²)
    # Space: O(n)


def main():
    result = three_sum_multi(arr = [1,1,2,2,3,3,4,4,5,5], target = 8)
    print(result) # 20

    result = three_sum_multi(arr = [1,1,2,2,2,2], target = 5)
    print(result) # 12

    result = three_sum_multi(arr = [2,1,3], target = 6)
    print(result) # 1

if __name__ == "__main__":
    main()

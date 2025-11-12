# ---------------------------
# 954. Array of Doubled Pairs
# ---------------------------

# Problem: https://leetcode.com/problems/array-of-doubled-pairs
#
# Given an integer array of even length arr, return true if it is possible to
# reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i <
# len(arr) / 2, or false otherwise.
# 
# Example 1:
# 
# Input: arr = [3,1,3,6]
# Output: false
# 
# Example 2:
# 
# Input: arr = [2,1,2,6]
# Output: false
# 
# Example 3:
# 
# Input: arr = [4,-2,2,-4]
# Output: true
# 
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
# [2,4,-2,-4].
# 
# 
# Constraints:
#         2 <= arr.length <= 3 * 10⁴
#         arr.length is even.
#         -10⁵ <= arr[i] <= 10⁵

from collections import Counter

# Solution: https://algo.monster/liteproblems/954
# Credit: AlgoMonster
def can_reorder_doubled(arr):
    # Count frequency of each element in the array
    frequency_map = Counter(arr)
    
    # Check if we have an odd number of zeros
    # Since 0 * 2 = 0, zeros can only pair with themselves
    # So we need an even count of zeros
    if frequency_map[0] % 2 == 1:
        return False
    
    # Sort elements by their absolute value
    # This ensures we process smaller absolute values first
    # For negative numbers: -4 needs -2, so we process -2 first
    # For positive numbers: 2 needs 4, so we process 2 first
    for current_value in sorted(frequency_map, key=abs):
        # Calculate the double of current value
        double_value = current_value * 2
        
        # Check if we have enough doubles to pair with current values
        if frequency_map[double_value] < frequency_map[current_value]:
            return False
        
        # Use up the doubles by pairing them with current values
        frequency_map[double_value] -= frequency_map[current_value]
    
    # If all elements can be paired successfully, return True
    return True
    # Time: O(n log(n))
    # Space: O(n)


def main():
    result = can_reorder_doubled(arr = [3,1,3,6])
    print(result) # False

    result = can_reorder_doubled(arr = [2,1,2,6])
    print(result) # False

    result = can_reorder_doubled(arr = [4,-2,2,-4])
    print(result) # True

if __name__ == "__main__":
    main()

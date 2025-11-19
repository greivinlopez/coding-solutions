# ----------------------------------------------------------------------
# 1526. Minimum Number of Increments on Subarrays to Form a Target Array
# ----------------------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array
#
# You are given an integer array target. You have an integer array initial of the
# same size as target with all elements initially zeros.
# 
# In one operation you can choose any subarray from initial and increment each
# value by one.
# 
# Return the minimum number of operations to form a target array from initial.
# 
# The test cases are generated so that the answer fits in a 32-bit integer.
# 
# Example 1:
# 
# Input: target = [1,2,3,2,1]
# Output: 3
# 
# Explanation: We need at least 3 operations to form the target array from the
# initial array.
# [0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
# [1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
# [1,2,2,2,1] increment 1 at index 2.
# [1,2,3,2,1] target array is formed.
# 
# Example 2:
# 
# Input: target = [3,1,1,2]
# Output: 4
# 
# Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
# 
# Example 3:
# 
# Input: target = [3,1,5,4,2]
# Output: 7
# 
# Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] ->
# [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
# 
# 
# Constraints:
#         1 <= target.length <= 10⁵
#         1 <= target[i] <= 10⁵
#         ​​​​​​​The input is generated such that the answer fits inside a 32 bit integer.


# Solution: https://algo.monster/liteproblems/1526
# Credit: AlgoMonster
def min_number_operations(target):
    # Start with the first element's height as initial operations needed
    total_operations = target[0]
    
    # For each consecutive pair, add the increase in height (if any)
    for i in range(1, len(target)):
        previous_height = target[i - 1]
        current_height = target[i]
        
        # Only add operations when height increases
        # If height decreases or stays same, no new operations needed
        height_increase = max(0, current_height - previous_height)
        total_operations += height_increase
    
    return total_operations
    # Time: O(n)
    # Space: O(1)

# One liner solution
# Solution: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/7312095/beats-99-explained-by-karanagnani-8a5i
# Credit: Breccan Harlow -> https://leetcode.com/u/breccan-harlow/
def min_number_operations_short(target):
    return sum(max(0, target[i] - target[i-1]) for i in range(1, len(target))) + target[0]
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_number_operations(target = [1,2,3,2,1])
    print(result) # 3

    result = min_number_operations(target = [3,1,1,2])
    print(result) # 4

    result = min_number_operations(target = [3,1,5,4,2])
    print(result) # 7

if __name__ == "__main__":
    main()

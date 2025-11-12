# -------------------------
# 941. Valid Mountain Array
# -------------------------

# Problem: https://leetcode.com/problems/valid-mountain-array
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
#         
#   * arr.length >= 3
#   * There exists some i with 0 < i < arr.length - 1 such that:       
#       * arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#       * arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png
# 
# Example 1:
# 
# Input: arr = [2,1]
# Output: false
# 
# Example 2:
# 
# Input: arr = [3,5,5]
# Output: false
# 
# Example 3:
# 
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         0 <= arr[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/941
# Credit: AlgoMonster
def valid_mountain_array(arr):
    n = len(arr)
    
    # Mountain array must have at least 3 elements
    if n < 3:
        return False
    
    # Use two pointers approach
    left_pointer = 0
    right_pointer = n - 1
    
    # Climb up from the left side
    # Stop when we reach peak or can't go further
    while left_pointer + 1 < n - 1 and arr[left_pointer] < arr[left_pointer + 1]:
        left_pointer += 1
    
    # Climb up from the right side (going backwards)
    # Stop when we reach peak or can't go further
    while right_pointer - 1 > 0 and arr[right_pointer - 1] > arr[right_pointer]:
        right_pointer -= 1
    
    # For a valid mountain, both pointers should meet at the same peak
    return left_pointer == right_pointer
    # Time: O(n)
    # Space: O(1)


def main():
    result = valid_mountain_array(arr = [2,1])
    print(result) # False

    result = valid_mountain_array(arr = [3,5,5])
    print(result) # False

    result = valid_mountain_array(arr = [0,3,2,1])
    print(result) # True

if __name__ == "__main__":
    main()

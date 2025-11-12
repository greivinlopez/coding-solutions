# --------------------
# 969. Pancake Sorting
# --------------------

# Problem: https://leetcode.com/problems/pancake-sorting
#
# Given an array of integers arr, sort the array by performing a series of pancake
# flips.
# 
# In one pancake flip we do the following steps:
#         
#   * Choose an integer k where 1 <= k <= arr.length.
#   * Reverse the sub-array arr[0...k-1] (0-indexed).
# 
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3,
# we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k
# = 3.
# 
# Return an array of the k-values corresponding to a sequence of pancake flips
# that sort arr. Any valid answer that sorts the array within 10 * arr.length
# flips will be judged as correct.
# 
# Example 1:
# 
# Input: arr = [3,2,4,1]
# Output: [4,2,4,3]
# 
# Explanation:
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: arr = [3, 2, 4, 1]
# After 1st flip (k = 4): arr = [1, 4, 2, 3]
# After 2nd flip (k = 2): arr = [4, 1, 2, 3]
# After 3rd flip (k = 4): arr = [3, 2, 1, 4]
# After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
# 
# Example 2:
# 
# Input: arr = [1,2,3]
# Output: []
# 
# Explanation: The input is already sorted, so there is no need to flip anything.
# Note that other answers, such as [3, 3], would also be accepted.
# 
# 
# Constraints:
#   1 <= arr.length <= 100
#   1 <= arr[i] <= arr.length
#   All integers in arr are unique (i.e. arr is a permutation of the integers 
#   from 1 to arr.length).


# Solution: https://algo.monster/liteproblems/969
# Credit: AlgoMonster
def pancake_sort(arr):
  
    def reverse_subarray(array, end_index):
        start_index = 0
        while start_index < end_index:
            # Swap elements at start and end positions
            array[start_index], array[end_index] = array[end_index], array[start_index]
            start_index += 1
            end_index -= 1
    
    array_length = len(arr)
    flip_sequence = []
    
    # Process each position from the end to the beginning
    for current_position in range(array_length - 1, 0, -1):
        # Find where the target value (current_position + 1) is located
        target_value = current_position + 1
        target_index = current_position
        
        # Search for the target value's current position
        while target_index > 0 and arr[target_index] != target_value:
            target_index -= 1
        
        # If the target value is not already in its correct position
        if target_index < current_position:
            # First flip: bring target value to the front (if not already there)
            if target_index > 0:
                flip_sequence.append(target_index + 1)
                reverse_subarray(arr, target_index)
            
            # Second flip: move target value to its final position
            flip_sequence.append(current_position + 1)
            reverse_subarray(arr, current_position)
    
    return flip_sequence
    # Time: O(n²)
    # Space: O(1)


def main():
    result = pancake_sort(arr = [3,2,4,1])
    print(result) # [3, 4, 2, 3, 2]

    result = pancake_sort(arr = [1,2,3])
    print(result) # []

if __name__ == "__main__":
    main()

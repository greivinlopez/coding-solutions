# ---------------------
# 1089. Duplicate Zeros
# ---------------------

# Problem: https://leetcode.com/problems/duplicate-zeros
#
# Given a fixed-length integer array arr, duplicate each occurrence of zero,
# shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written. Do
# the above modifications to the input array in place and do not return anything.
# 
# Example 1:
# 
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# 
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# Example 2:
# 
# Input: arr = [1,2,3]
# Output: [1,2,3]
# 
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         0 <= arr[i] <= 9


# Solution: https://algo.monster/liteproblems/1089
# Credit: AlgoMonster
def duplicate_zeros(arr):
    n = len(arr)
    
    # First pass: Find how many elements from original array will fit
    # source_index tracks position in original array
    # dest_position tracks position in modified array
    source_index = -1
    dest_position = 0
    
    while dest_position < n:
        source_index += 1
        # If current element is 0, it takes 2 positions, otherwise 1
        if arr[source_index] == 0:
            dest_position += 2
        else:
            dest_position += 1
    
    # Start filling from the end of array
    write_position = n - 1
    
    # Handle edge case: if last zero would overflow array bounds
    # Only write one zero at the end instead of duplicating
    if dest_position == n + 1:
        arr[write_position] = 0
        source_index -= 1
        write_position -= 1
    
    # Second pass: Fill array from right to left
    # Using ~write_position as condition (equivalent to write_position >= 0)
    while write_position >= 0:
        if arr[source_index] == 0:
            # Duplicate the zero
            arr[write_position] = 0
            arr[write_position - 1] = 0
            write_position -= 1
        else:
            # Copy non-zero element
            arr[write_position] = arr[source_index]
        
        source_index -= 1
        write_position -= 1
    # Time: O(n)
    # Space: O(1)


def main():
    arr1 = [1,0,2,3,0,4,5,0]
    duplicate_zeros(arr1)
    print(arr1) # [1, 0, 0, 2, 3, 0, 0, 4]

    arr2 = [1,2,3]
    duplicate_zeros(arr2)
    print(arr2) # [1, 2, 3]

if __name__ == "__main__":
    main()

# -------------------------------------------------
# 1640. Check Array Formation Through Concatenation
# -------------------------------------------------

# Problem: https://leetcode.com/problems/check-array-formation-through-concatenation
#
# You are given an array of distinct integers arr and an array of integer arrays
# pieces, where the integers in pieces are distinct. Your goal is to form arr by
# concatenating the arrays in pieces in any order. However, you are not allowed to
# reorder the integers in each array pieces[i].
# 
# Return true if it is possible to form the array arr from pieces. Otherwise,
# return false.
# 
# Example 1:
# 
# Input: arr = [15,88], pieces = [[88],[15]]
# Output: true
# 
# Explanation: Concatenate [15] then [88]
# 
# Example 2:
# 
# Input: arr = [49,18,16], pieces = [[16,18,49]]
# Output: false
# 
# Explanation: Even though the numbers match, we cannot reorder pieces[0].
# 
# Example 3:
# 
# Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
# Output: true
# 
# Explanation: Concatenate [91] then [4,64] then [78]
# 
# 
# Constraints:
#   1 <= pieces.length <= arr.length <= 100
#   sum(pieces[i].length) == arr.length
#   1 <= pieces[i].length <= arr.length
#   1 <= arr[i], pieces[i][j] <= 100
#   The integers in arr are distinct.
#   The integers in pieces are distinct (i.e., If we flatten pieces in a 1D
#   array, all the integers in this array are distinct).


# Solution: https://algo.monster/liteproblems/1640
# Credit: AlgoMonster
def can_form_array(arr, pieces):
    # Current index in the target array
    arr_index = 0
    
    # Iterate through the target array
    while arr_index < len(arr):
        # Find a piece that starts with current element in arr
        piece_index = 0
        while piece_index < len(pieces) and pieces[piece_index][0] != arr[arr_index]:
            piece_index += 1
        
        # If no matching piece found, cannot form the array
        if piece_index == len(pieces):
            return False
        
        # Verify that the found piece matches consecutive elements in arr
        element_index = 0
        while (element_index < len(pieces[piece_index]) and 
                arr_index < len(arr) and 
                arr[arr_index] == pieces[piece_index][element_index]):
            arr_index += 1
            element_index += 1
        
        # If piece wasn't fully matched, array cannot be formed
        if element_index != len(pieces[piece_index]):
            return False
    
    # All elements in arr were successfully matched
    return True
    # Time: O(n * m)
    # Space: O(1)


def main():
    result = can_form_array(arr = [15,88], pieces = [[88],[15]])
    print(result) # True

    result = can_form_array(arr = [49,18,16], pieces = [[16,18,49]])
    print(result) # False

    result = can_form_array(arr = [91,4,64,78], pieces = [[78],[4,64],[91]])
    print(result) # True

if __name__ == "__main__":
    main()

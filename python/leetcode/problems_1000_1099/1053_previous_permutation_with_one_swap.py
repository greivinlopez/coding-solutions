# ----------------------------------------
# 1053. Previous Permutation With One Swap
# ----------------------------------------

# Problem: https://leetcode.com/problems/previous-permutation-with-one-swap
#
# Given an array of positive integers arr (not necessarily distinct), return the
# lexicographically largest permutation that is smaller than arr, that can be made
# with exactly one swap. If it cannot be done, then return the same array.
# 
# Note that a swap exchanges the positions of two numbers arr[i] and arr[j]
# 
# Example 1:
# 
# Input: arr = [3,2,1]
# Output: [3,1,2]
# 
# Explanation: Swapping 2 and 1.
# 
# Example 2:
# 
# Input: arr = [1,1,5]
# Output: [1,1,5]
# 
# Explanation: This is already the smallest permutation.
# 
# Example 3:
# 
# Input: arr = [1,9,4,6,7]
# Output: [1,7,4,6,9]
# 
# Explanation: Swapping 9 and 7.
# 
# 
# Constraints:
#         1 <= arr.length <= 10⁴
#         1 <= arr[i] <= 10⁴


# Solution: https://algo.monster/liteproblems/1053
# Credit: AlgoMonster
def prev_perm_opt1(arr):
    n = len(arr)
    
    # Traverse from right to left to find the first position where arr[i-1] > arr[i]
    # This is the position where we can make a swap to get a smaller permutation
    for i in range(n - 1, 0, -1):
        if arr[i - 1] > arr[i]:
            # Found a position where the previous element is greater than current
            # Now find the best element to swap with arr[i-1]
            
            # Traverse from right to find the largest element that is:
            # 1. Smaller than arr[i-1] (to ensure smaller permutation)
            # 2. Not equal to its previous element (to avoid duplicate swaps)
            for j in range(n - 1, i - 1, -1):
                if arr[j] < arr[i - 1] and arr[j] != arr[j - 1]:
                    # Swap the elements to get the largest smaller permutation
                    arr[i - 1], arr[j] = arr[j], arr[i - 1]
                    return arr
    
    # No valid swap found, return the original array
    return arr
    # Time: O(n)
    # Space: O(1)


def main():
    result = prev_perm_opt1(arr = [3,2,1])
    print(result) # [3, 1, 2]

    result = prev_perm_opt1(arr = [1,1,5])
    print(result) # [1, 1, 5]

    result = prev_perm_opt1(arr = [1,9,4,6,7])
    print(result) # [1, 7, 4, 6, 9]

if __name__ == "__main__":
    main()

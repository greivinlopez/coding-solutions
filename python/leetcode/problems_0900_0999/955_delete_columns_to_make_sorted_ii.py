# -------------------------------------
# 955. Delete Columns to Make Sorted II
# -------------------------------------

# Problem: https://leetcode.com/problems/delete-columns-to-make-sorted-ii
#
# You are given an array of n strings strs, all of the same length.
# 
# We may choose any deletion indices, and we delete all the characters in those
# indices for each string.
# 
# For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2,
# 3}, then the final array after deletions is ["bef", "vyz"].
# 
# Suppose we chose a set of deletion indices answer such that after deletions, the
# final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <=
# strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of
# answer.length.
# 
# Example 1:
# 
# Input: strs = ["ca","bb","ac"]
# Output: 1
# 
# Explanation:
# After deleting the first column, strs = ["a", "b", "c"].
# Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
# We require at least 1 deletion since initially strs was not in lexicographic
# order, so the answer is 1.
# 
# Example 2:
# 
# Input: strs = ["xc","yb","za"]
# Output: 0
# 
# Explanation:
# strs is already in lexicographic order, so we do not need to delete anything.
# Note that the rows of strs are not necessarily in lexicographic order:
# i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
# 
# Example 3:
# 
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# 
# Explanation: We have to delete every column.
# 
# 
# Constraints:
#         n == strs.length
#         1 <= n <= 100
#         1 <= strs[i].length <= 100
#         strs[i] consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/955
# Credit: AlgoMonster
def min_deletion_size(strs):
    # Handle edge cases: empty list or single string list
    if not strs or len(strs) <= 1:
        return 0
    
    num_strings = len(strs)
    string_length = len(strs[0])
    deleted_columns = 0
    
    # Track which pairs of adjacent strings are already sorted
    # If sorted[i] is True, it means A[i] < A[i+1] lexicographically
    sorted_pairs = [False] * num_strings
    
    # Process each column from left to right
    for col in range(string_length):
        # Check if current column should be deleted
        # A column must be deleted if it breaks the sorting order
        should_delete = False
        
        for row in range(num_strings - 1):
            # Only check pairs that aren't already determined to be sorted
            if not sorted_pairs[row] and strs[row][col] > strs[row + 1][col]:
                # Column breaks sorting order, must delete it
                deleted_columns += 1
                should_delete = True
                break  # Skip to next column
        
        # If column was deleted, continue to next column
        if should_delete:
            continue
        
        # Column is valid, update sorted status for string pairs
        # Mark pairs as sorted if current column makes them strictly increasing
        for row in range(num_strings - 1):
            if strs[row][col] < strs[row + 1][col]:
                sorted_pairs[row] = True
    
    return deleted_columns
    # Time: O(n * m)
    # Space: O(n)


def main():
    result = min_deletion_size(strs = ["ca","bb","ac"])
    print(result) # 1

    result = min_deletion_size(strs = ["xc","yb","za"])
    print(result) # 0

    result = min_deletion_size(strs = ["zyx","wvu","tsr"])
    print(result) # 3

if __name__ == "__main__":
    main()

# ----------------------------------
# 944. Delete Columns to Make Sorted
# ----------------------------------

# Problem: https://leetcode.com/problems/delete-columns-to-make-sorted
#
# You are given an array of n strings strs, all of the same length.
# 
# The strings can be arranged such that there is one on each line, making a grid.
#         
#   * For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
#       abc
#       bce
#       cae
# 
# You want to delete the columns that are not sorted lexicographically. In the
# above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are
# sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
# 
# Return the number of columns that you will delete.
# 
# Example 1:
# 
# Input: strs = ["cba","daf","ghi"]
# Output: 1
# 
# Explanation: The grid looks as follows:
#   cba
#   daf
#   ghi
# Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1
# column.
# 
# Example 2:
# 
# Input: strs = ["a","b"]
# Output: 0
# 
# Explanation: The grid looks as follows:
#   a
#   b
# Column 0 is the only column and is sorted, so you will not delete any columns.
# 
# Example 3:
# 
# Input: strs = ["zyx","wvu","tsr"]
# Output: 3
# 
# Explanation: The grid looks as follows:
#   zyx
#   wvu
#   tsr
# All 3 columns are not sorted, so you will delete all 3.
# 
# 
# Constraints:
#         n == strs.length
#         1 <= n <= 100
#         1 <= strs[i].length <= 1000
#         strs[i] consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/944
# Credit: AlgoMonster
def min_deletion_size(strs):
    # Get dimensions: number of columns (string length) and rows (number of strings)
    num_cols = len(strs[0])
    num_rows = len(strs)
    
    # Counter for columns that need to be deleted
    columns_to_delete = 0
    
    # Check each column
    for col_idx in range(num_cols):
        # Check if current column is sorted by comparing adjacent elements
        for row_idx in range(1, num_rows):
            # If current character is less than previous character in same column,
            # the column is not sorted and must be deleted
            if strs[row_idx][col_idx] < strs[row_idx - 1][col_idx]:
                columns_to_delete += 1
                break  # No need to check rest of column once we find it's unsorted
    
    return columns_to_delete
    # Time: O(m * n)
    # Space: O(1)


def main():
    result = min_deletion_size(strs = ["cba","daf","ghi"])
    print(result) # 1

    result = min_deletion_size(strs = ["a","b"])
    print(result) # 0

    result = min_deletion_size(strs = ["zyx","wvu","tsr"])
    print(result) # 3

if __name__ == "__main__":
    main()

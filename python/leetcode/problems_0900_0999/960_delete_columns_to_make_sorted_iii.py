# --------------------------------------
# 960. Delete Columns to Make Sorted III
# --------------------------------------

# Problem: https://leetcode.com/problems/delete-columns-to-make-sorted-iii
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
# final array has every string (row) in lexicographic order. (i.e., (strs[0][0] <=
# strs[0][1] <= ... <= strs[0][strs[0].length - 1]), and (strs[1][0] <= strs[1][1]
# <= ... <= strs[1][strs[1].length - 1]), and so on). Return the minimum possible
# value of answer.length.
# 
# Example 1:
# 
# Input: strs = ["babca","bbazb"]
# Output: 3
# 
# Explanation: After deleting columns 0, 1, and 4, the final array is strs =
# ["bc", "az"].
# Both these rows are individually in lexicographic order (ie. strs[0][0] <=
# strs[0][1] and strs[1][0] <= strs[1][1]).
# Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic
# order.
# 
# Example 2:
# 
# Input: strs = ["edcba"]
# Output: 4
# 
# Explanation: If we delete less than 4 columns, the only row will not be
# lexicographically sorted.
# 
# Example 3:
# 
# Input: strs = ["ghi","def","abc"]
# Output: 0
# 
# Explanation: All rows are already lexicographically sorted.
# 
# 
# Constraints:
#         n == strs.length
#         1 <= n <= 100
#         1 <= strs[i].length <= 100
#         strs[i] consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/960
# Credit: AlgoMonster
def min_deletion_size(strs):
    # Get the length of each string (all strings have same length)
    string_length = len(strs[0])
    
    # dp[i] represents the maximum length of increasing subsequence ending at column i
    # Initialize all positions with 1 (each column itself forms a subsequence of length 1)
    dp = [1] * string_length
    
    # For each column position
    for current_col in range(string_length):
        # Check all previous columns
        for prev_col in range(current_col):
            # Check if we can extend the subsequence from prev_col to current_col
            # This is valid if for ALL strings, character at prev_col <= character at current_col
            if all(string[prev_col] <= string[current_col] for string in strs):
                # Update the maximum subsequence length ending at current_col
                dp[current_col] = max(dp[current_col], dp[prev_col] + 1)
    
    # The minimum columns to delete = total columns - maximum columns we can keep
    return string_length - max(dp)
    # Time: O(n² * m)
    # Space: O(n)


def main():
    result = min_deletion_size(strs = ["babca","bbazb"])
    print(result) # 3

    result = min_deletion_size(strs = ["edcba"])
    print(result) # 4

    result = min_deletion_size(strs = ["ghi","def","abc"])
    print(result) # 0

if __name__ == "__main__":
    main()

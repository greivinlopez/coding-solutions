# ---------------------------------------------------------
# 1312. Minimum Insertion Steps to Make a String Palindrome
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome
#
# Given a string s. In one step you can insert any character at any index of the
# string.
# 
# Return the minimum number of steps to make s palindrome.
# 
# A Palindrome String is one that reads the same backward as well as forward.
# 
# Example 1:
# 
# Input: s = "zzazz"
# Output: 0
# 
# Explanation: The string "zzazz" is already palindrome we do not need any
# insertions.
# 
# Example 2:
# 
# Input: s = "mbadm"
# Output: 2
# 
# Explanation: String can be "mbdadbm" or "mdbabdm".
# 
# Example 3:
# 
# Input: s = "leetcode"
# Output: 5
# 
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# 
# 
# Constraints:
#         1 <= s.length <= 500
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1312
# Credit: AlgoMonster
def min_insertions(s):
    from functools import cache
    
    @cache
    def dfs(left, right):
        # Base case: single character or empty substring is already palindrome
        if left >= right:
            return 0
        
        # If characters at both ends match, no insertion needed for these positions
        if s[left] == s[right]:
            return dfs(left + 1, right - 1)
        
        # Characters don't match, need to insert
        # Either insert s[right] at beginning or s[left] at end
        insert_at_left = dfs(left, right - 1)  # Insert s[right] before s[left]
        insert_at_right = dfs(left + 1, right)  # Insert s[left] after s[right]
        
        return 1 + min(insert_at_left, insert_at_right)
    
    # Start with entire string
    return dfs(0, len(s) - 1)
    # Time: O(n²)
    # Space: O(n²)


def main():
    result = min_insertions(s = "zzazz")
    print(result) # 0

    result = min_insertions(s = "mbadm")
    print(result) # 2

    result = min_insertions(s = "leetcode")
    print(result) # 5

if __name__ == "__main__":
    main()

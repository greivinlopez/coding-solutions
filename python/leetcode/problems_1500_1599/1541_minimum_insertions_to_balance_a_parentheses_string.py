# --------------------------------------------------------
# 1541. Minimum Insertions to Balance a Parentheses String
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string
#
# Given a parentheses string s containing only the characters '(' and ')'. A
# parentheses string is balanced if:
#         
#   * Any left parenthesis '(' must have a corresponding two consecutive right
#     parenthesis '))'.
#   * Left parenthesis '(' must go before the corresponding two consecutive
#     right parenthesis '))'.
# 
# In other words, we treat '(' as an opening parenthesis and '))' as a closing
# parenthesis.
#         
#   * For example, "())", "())(())))" and "(())())))" are balanced, ")()",
#     "()))" and "(()))" are not balanced.
# 
# You can insert the characters '(' and ')' at any position of the string to
# balance it if needed.
# 
# Return the minimum number of insertions needed to make s balanced.
# 
# Example 1:
# 
# Input: s = "(()))"
# Output: 1
# 
# Explanation: The second '(' has two matching '))', but the first '(' has only
# ')' matching. We need to add one more ')' at the end of the string to be
# "(())))" which is balanced.
# 
# Example 2:
# 
# Input: s = "())"
# Output: 0
# 
# Explanation: The string is already balanced.
# 
# Example 3:
# 
# Input: s = "))())("
# Output: 3
# 
# Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of '(' and ')' only.


# Solution: https://algo.monster/liteproblems/1541
# Credit: AlgoMonster
def min_insertions(s):
    # Track the number of insertions needed
    insertions_needed = 0
    # Track the number of unmatched left parentheses
    unmatched_left_parens = 0
    
    # Index for traversing the string
    index = 0
    string_length = len(s)
    
    while index < string_length:
        if s[index] == '(':
            # Found a left parenthesis, increment unmatched count
            unmatched_left_parens += 1
        else:
            # Found a right parenthesis, check if there's another one following
            if index < string_length - 1 and s[index + 1] == ')':
                # Found two consecutive right parentheses, move index forward
                index += 1
            else:
                # Only one right parenthesis, need to insert another one
                insertions_needed += 1
            
            # Now we have a pair of right parentheses (either found or inserted)
            if unmatched_left_parens == 0:
                # No left parenthesis to match with, need to insert one
                insertions_needed += 1
            else:
                # Match with an existing left parenthesis
                unmatched_left_parens -= 1
        
        # Move to the next character
        index += 1
    
    # After traversing, if there are still unmatched left parentheses,
    # each needs two right parentheses inserted (hence multiply by 2)
    insertions_needed += unmatched_left_parens * 2
    
    return insertions_needed
    # Time: O(n)
    # Space: O(1)


def main():
    result = min_insertions(s = "(()))")
    print(result) # 1

    result = min_insertions(s = "())")
    print(result) # 0

    result = min_insertions(s = "))())(")
    print(result) # 3

if __name__ == "__main__":
    main()

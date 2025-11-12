# ------------------------------------------------------------
# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
# ------------------------------------------------------------

# Problem: https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings
#
# A string is a valid parentheses string (denoted VPS) if and only if it consists
# of "(" and ")" characters only, and:
#         
#   * It is the empty string, or
#   * It can be written as AB (A concatenated with B), where A and B areVPS's, or
#   * It can be written as (A), where A is a VPS.
# 
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
#         
#   * depth("") = 0
#   * depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
#   * depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# 
# For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1,
# and 2), and ")(" and "(()" are not VPS's.
# 
# Given a VPS seq, split it into two disjoint subsequences A and B, such that A
# and B are VPS's (and A.length + B.length = seq.length).
# 
# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum
# possible value.
# 
# Return an answer array (of length seq.length) that encodes such a choice of A
# and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that
# even though multiple answers may exist, you may return any of them.
# 
# Example 1:
# 
# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]
# 
# Example 2:
# 
# Input: seq = "()(())()"
# Output: [0,0,0,1,1,0,1,1]
# 
# 
# Constraints:
#         1 <= seq.size <= 10000


# Solution: https://algo.monster/liteproblems/1111
# Credit: AlgoMonster
def max_depth_after_split(seq):
    # Initialize result array to store group assignments (0 or 1)
    result = [0] * len(seq)
    
    # Track current depth/nesting level of parentheses
    depth = 0
    
    # Iterate through each character in the sequence
    for index, char in enumerate(seq):
        if char == "(":
            # For opening parenthesis:
            # Assign to group 0 if depth is even, group 1 if odd
            result[index] = depth & 1
            # Increase depth after opening parenthesis
            depth += 1
        else:  # char == ")"
            # For closing parenthesis:
            # Decrease depth first (matching the corresponding opening)
            depth -= 1
            # Assign to same group as its matching opening parenthesis
            result[index] = depth & 1
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = max_depth_after_split(seq = "(()())")
    print(result) # [0, 1, 1, 1, 1, 0]

    result = max_depth_after_split(seq = "()(())()")
    print(result) # [0, 0, 0, 1, 1, 0, 0, 0]

if __name__ == "__main__":
    main()

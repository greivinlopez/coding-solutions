# ------------------------------------------------
# 2116. Check if a Parentheses String Can Be Valid
# ------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid
#
# A parentheses string is a non-empty string consisting only of '(' and ')'. It is
# valid if any of the following conditions is true:
# 
#   * It is ().
#   * It can be written as AB (A concatenated with B), where A and B are valid
#     parentheses strings.
#   * It can be written as (A), where A is a valid parentheses string.
# 
# You are given a parentheses string s and a string locked, both of length n.
# locked is a binary string consisting only of '0's and '1's. For each index i of
# locked,
# 
#   * If locked[i] is '1', you cannot change s[i].
#   * But if locked[i] is '0', you can change s[i] to either '(' or ')'.
# 
# Return true if you can make s a valid parentheses string. Otherwise, return
# false.
# 
# Example 1:
# 
# Input: s = "))()))", locked = "010100"
# Output: true
# 
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or
# s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s
# valid.
# 
# Example 2:
# 
# Input: s = "()()", locked = "0000"
# Output: true
# 
# Explanation: We do not need to make any changes because s is already valid.
# 
# Example 3:
# 
# Input: s = ")", locked = "0"
# Output: false
# 
# Explanation: locked permits us to change s[0].
# Changing s[0] to either '(' or ')' will not make s valid.
# 
# Example 4:
# 
# Input: s = "(((())(((())", locked = "111111010111"
# Output: true
# 
# Explanation: locked permits us to change s[6] and s[8].
# We change s[6] and s[8] to ')' to make s valid.
# 
# 
# Constraints:
#         n == s.length == locked.length
#         1 <= n <= 10^5
#         s[i] is either '(' or ')'.
#         locked[i] is either '0' or '1'.


# Solution: https://youtu.be/KMIIGDiXLhY
# Credit: Navdeep Singh founder of NeetCode
def can_be_valid(s, locked):
    if len(s) % 2 == 1:
        return False
    
    locked_cnt = 0
    unlocked_cnt = 0

    # Match closing parenthesis )
    for i in range(len(s)):
        if locked[i] == "0":
            unlocked_cnt += 1
        elif s[i] == "(":
            locked_cnt += 1
        else:
            if locked_cnt:
                locked_cnt -= 1
            elif unlocked_cnt:
                unlocked_cnt -= 1
            else:
                return False
    
    if locked_cnt == 0:
        return True
    
    locked_cnt = 0
    unlocked_cnt = 0

    # Match opening parenthesis (
    for i in reversed(range(len(s))):
        if locked[i] == "0":
            unlocked_cnt += 1
        elif s[i] == ")":
            locked_cnt += 1
        else:
            if locked_cnt:
                locked_cnt -= 1
            elif unlocked_cnt:
                unlocked_cnt -= 1
            else:
                return False

    return True
    # Time: O(n)
    # Space: O(1)


def main():
    result = can_be_valid(s = "))()))", locked = "010100")
    print(result) # True

    result = can_be_valid(s = "()()", locked = "0000")
    print(result) # True

    result = can_be_valid(s = ")", locked = "0")
    print(result) # False

    result = can_be_valid(s = "(((())(((())", locked = "111111010111")
    print(result) # True

if __name__ == "__main__":
    main()

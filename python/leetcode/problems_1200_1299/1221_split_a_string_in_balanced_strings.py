# ----------------------------------------
# 1221. Split a String in Balanced Strings
# ----------------------------------------

# Problem: https://leetcode.com/problems/split-a-string-in-balanced-strings
#
# Balanced strings are those that have an equal quantity of 'L' and 'R'
# characters.
# 
# Given a balanced string s, split it into some number of substrings such that:
#         
#   * Each substring is balanced.
# 
# Return the maximum number of balanced strings you can obtain.
# 
# Example 1:
# 
# Input: s = "RLRRLLRLRL"
# Output: 4
# 
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring
# contains same number of 'L' and 'R'.
# 
# Example 2:
# 
# Input: s = "RLRRRLLRLL"
# Output: 2
# 
# Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same
# number of 'L' and 'R'.
# Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd
# and 5th substrings are not balanced.
# 
# Example 3:
# 
# Input: s = "LLLLRRRR"
# Output: 1
# 
# Explanation: s can be split into "LLLLRRRR".
# 
# 
# Constraints:
#         2 <= s.length <= 1000
#         s[i] is either 'L' or 'R'.
#         s is a balanced string.


# Solution: https://algo.monster/liteproblems/1221
# Credit: AlgoMonster
def balanced_string_split(s):
    # Initialize counter for balanced substrings and balance tracker
    balanced_count = 0
    balance = 0
    
    # Iterate through each character in the string
    for char in s:
        # Increment balance for 'L', decrement for 'R'
        if char == 'L':
            balance += 1
        else:  # char == 'R'
            balance -= 1
        
        # When balance reaches 0, we have a balanced substring
        if balance == 0:
            balanced_count += 1
    
    return balanced_count
    # Time: O(n)
    # Space: O(1)


def main():
    result = balanced_string_split(s = "RLRRLLRLRL")
    print(result) # 4

    result = balanced_string_split(s = "RLRRRLLRLL")
    print(result) # 2

    result = balanced_string_split(s = "LLLLRRRR")
    print(result) # 1

if __name__ == "__main__":
    main()

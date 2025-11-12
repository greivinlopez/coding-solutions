# ----------------------------------------------
# 1047. Remove All Adjacent Duplicates In String
# ----------------------------------------------

# Problem: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string
#
# You are given a string s consisting of lowercase English letters. A duplicate
# removal consists of choosing two adjacent and equal letters and removing them.
# 
# We repeatedly make duplicate removals on s until we no longer can.
# 
# Return the final string after all such duplicate removals have been made. It can
# be proven that the answer is unique.
# 
# Example 1:
# 
# Input: s = "abbaca"
# Output: "ca"
# 
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and
# equal, and this is the only possible move.  The result of this move is that the
# string is "aaca", of which only "aa" is possible, so the final string is "ca".
# 
# Example 2:
# 
# Input: s = "azxxzy"
# Output: "ay"
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s consists of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1047
# Credit: AlgoMonster
def remove_duplicates(s):
    # Use a stack to track characters
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If stack is not empty and top element equals current character
        if stack and stack[-1] == char:
            # Remove the duplicate by popping from stack
            stack.pop()
        else:
            # Add the character to stack if no duplicate found
            stack.append(char)
    
    # Join all remaining characters in stack to form the result
    return ''.join(stack)
    # Time: O(n)
    # Space: O(n)


def main():
    result = remove_duplicates(s = "abbaca")
    print(result) # "ca"

    result = remove_duplicates(s = "azxxzy")
    print(result) # "ay"

if __name__ == "__main__":
    main()

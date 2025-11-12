# ---------------------------
# 1544. Make The String Great
# ---------------------------

# Problem: https://leetcode.com/problems/make-the-string-great
#
# Given a string s of lower and upper case English letters.
# 
# A good string is a string which doesn't have two adjacent characters s[i] and
# s[i + 1] where:
# 
#   * 0 <= i <= s.length - 2
#   * s[i] is a lower-case letter and s[i + 1] is the same letter but in
#     upper-case or vice-versa.
# 
# To make the string good, you can choose two adjacent characters that make the
# string bad and remove them. You can keep doing this until the string becomes
# good.
# 
# Return the string after making it good. The answer is guaranteed to be unique
# under the given constraints.
# 
# Notice that an empty string is also good.
# 
# Example 1:
# 
# Input: s = "leEeetcode"
# Output: "leetcode"
# 
# Explanation: In the first step, either you choose i = 1 or i = 2, both will
# result "leEeetcode" to be reduced to "leetcode".
# 
# Example 2:
# 
# Input: s = "abBAcC"
# Output: ""
# 
# Explanation: We have many possible scenarios, and all lead to the same answer.
# For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
# 
# Example 3:
# 
# Input: s = "s"
# Output: "s"
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s contains only lower and upper case English letters.


# Solution: https://youtu.be/10tBWNjzvtw
# Credit: Navdeep Singh founder of NeetCode
def make_good(s):
    def lower(c):
        if ord(c) < ord('a'):
            return chr(ord('a') + ord(c) - ord('A'))
        return c

    stack = []
    i = 0
    while i < len(s):
        if (
            stack and
            stack[-1] != s[i] and
            lower(stack[-1]) == lower(s[i])
        ):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1
    
    return "".join(stack)
    # Time: O(n)
    # Space: O(n)


def main():
    result = make_good("leEeetcode")
    print(result) # "leetcode"

    result = make_good("abBAcC")
    print(result) # ""

    result = make_good("s")
    print(result) # "s"

if __name__ == "__main__":
    main()

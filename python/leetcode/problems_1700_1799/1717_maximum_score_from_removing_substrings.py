# --------------------------------------------
# 1717. Maximum Score From Removing Substrings
# --------------------------------------------

# Problem: https://leetcode.com/problems/maximum-score-from-removing-substrings
#
# You are given a string s and two integers x and y. You can perform two types of
# operations any number of times.
#         
#   * Remove substring "ab" and gain x points.
#     For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#         
#   * Remove substring "ba" and gain y points.
#     For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# 
# Return the maximum points you can gain after applying the above operations on s.
# 
# Example 1:
# 
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# 
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5
# points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points
# are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are
# added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added
# to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# 
# Example 2:
# 
# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20
# 
# 
# Constraints:
#         1 <= s.length <= 10^5
#         1 <= x, y <= 10^4
#         s consists of lowercase English letters.


# Solution: https://youtu.be/r_3a0oG1VcY
# Credit: Navdeep Singh founder of NeetCode
def maximum_gain(s, x, y):
    def remove_pairs(pair, score):
        nonlocal s
        res = 0
        stack = []
        for c in s:
            if c == pair[1] and stack and stack[-1] == pair[0]:
                stack.pop()
                res += score
            else:
                stack.append(c)
        s = "".join(stack)
        return res
    
    res = 0
    pair = "ab" if x > y else "ba"
    res += remove_pairs(pair, max(x, y))
    res += remove_pairs(pair[::-1], min(x, y))
    return res
    # Time: O(n) 
    # Space: O(n)


def main():
    result = maximum_gain(s = "cdbcbbaaabab", x = 4, y = 5)
    print(result) # 19

    result = maximum_gain(s = "aabbaaxybbaabb", x = 5, y = 4)
    print(result) # 20

if __name__ == "__main__":
    main()

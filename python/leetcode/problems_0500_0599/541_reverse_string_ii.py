# ----------------------
# 541. Reverse String II
# ----------------------

# Problem: https://leetcode.com/problems/reverse-string-ii
#
# Given a string s and an integer k, reverse the first k characters for every 2k
# characters counting from the start of the string.
# 
# If there are fewer than k characters left, reverse all of them. If there are
# less than 2k but greater than or equal to k characters, then reverse the first k
# characters and leave the other as original.
# 
# Example 1:
# 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# 
# Example 2:
# 
# Input: s = "abcd", k = 2
# Output: "bacd"
# 
# 
# Constraints:
#         1 <= s.length <= 10⁴
#         s consists of only lowercase English letters.
#         1 <= k <= 10⁴


# Solution: https://leetcode.com/problems/reverse-string-ii/solutions/100890/python-straightforward-with-explanation
# Credit: Alex Wice -> https://leetcode.com/u/awice/
def reverse_str(s, k):
    s = list(s)
    for i in range(0, len(s), 2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)
    # Time: O(n)
    # Space: O(n)


def main():
    result = reverse_str(s = "abcdefg", k = 2)
    print(result) # "bacdfeg"

    result = reverse_str(s = "abcd", k = 2)
    print(result) # "bacd"

if __name__ == "__main__":
    main()

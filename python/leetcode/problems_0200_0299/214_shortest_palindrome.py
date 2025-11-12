# ------------------------
# 214. Shortest Palindrome
# ------------------------

# Problem: https://leetcode.com/problems/shortest-palindrome
#
# You are given a string s. You can convert s to a palindrome by adding characters
# in front of it.
# 
# Return the shortest palindrome you can find by performing this transformation.
# 
# Example 1:
# 
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# 
# Example 2:
# 
# Input: s = "abcd"
# Output: "dcbabcd"
# 
# 
# Constraints:
#         0 <= s.length <= 5 * 10^4
#         s consists of lowercase English letters only.


# Solution: https://youtu.be/niOT-FK1RH8
# Credit: Navdeep Singh founder of NeetCode
def shortest_palindrome(s):
    prefix = 0
    suffix = 0
    base = 29
    last_index = -1
    power = 1
    mod = 10**9 + 7

    for i, c in enumerate(s):
        char = (ord(c) - ord('a') + 1)
        
        prefix = (prefix * base + char) % mod
        suffix = (suffix + char * power) % mod
        power = (power * base) % mod

        if prefix == suffix:
            last_index = i

    suffix = s[last_index + 1:]
    return suffix[::-1] + s
    # Time: O(n)
    # Space: O(n)


def main():
    result = shortest_palindrome("aacecaaa")
    print(result) # "aaacecaaa"

    result = shortest_palindrome("abcd")
    print(result) # "dcbabcd"

if __name__ == "__main__":
    main()

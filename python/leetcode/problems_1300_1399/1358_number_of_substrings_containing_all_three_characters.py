# ----------------------------------------------------------
# 1358. Number of Substrings Containing All Three Characters
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters
#
# Given a string s consisting only of characters a, b and c.
# 
# Return the number of substrings containing at least one occurrence of all these
# characters a, b and c.
# 
# Example 1:
# 
# Input: s = "abcabc"
# Output: 10
# 
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again).
# 
# Example 2:
# 
# Input: s = "aaacb"
# Output: 3
# 
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb".
# 
# Example 3:
# 
# Input: s = "abc"
# Output: 1
# 
# 
# Constraints:
#         3 <= s.length <= 5 x 10^4
#         s only consists of a, b or c characters.


# Solution: https://youtu.be/iSf7d2ldp70
# Credit: Navdeep Singh founder of NeetCode
def number_of_substrings(s):
    l = 0
    res = 0
    count = [0] * 3
    
    for r in range(len(s)):
        count[ord(s[r]) - ord("a")] += 1
        
        while count[0] and count[1] and count[2]:
            res += (len(s) - r)
            count[ord(s[l]) - ord("a")] -= 1
            l += 1
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = number_of_substrings("abcabc")
    print(result) # 10

    result = number_of_substrings("aaacb")
    print(result) # 3

    result = number_of_substrings("abc")
    print(result) # 1

if __name__ == "__main__":
    main()

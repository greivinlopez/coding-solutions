# -----------------------------
# 844. Backspace String Compare
# -----------------------------

# Problem: https://leetcode.com/problems/backspace-string-compare
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
# 
# Note that after backspacing an empty text, the text will continue empty.
# 
# Example 1:
# 
# Input: s = "ab#c", t = "ad#c"
# Output: true
# 
# Explanation: Both s and t become "ac".
# 
# Example 2:
# 
# Input: s = "ab##", t = "c#d#"
# Output: true
# 
# Explanation: Both s and t become "".
# 
# Example 3:
# 
# Input: s = "a#c", t = "b"
# Output: false
# 
# Explanation: s becomes "c" while t becomes "b".
# 
# 
# Constraints:
#         1 <= s.length, t.length <= 200
#         s and t only contain lowercase letters and '#' characters.
# 
# Follow up: Can you solve it in O(n) time and O(1) space?


# Solution: https://youtu.be/k2qrymM_DOo
# Credit: Navdeep Singh founder of NeetCode
def backspace_compare(s, t):
    def next_valid_char(string, index):
        backspace = 0
        while index >= 0:
            if backspace == 0 and string[index] != "#":
                break
            elif string[index] == "#":
                backspace += 1
            else:
                backspace -= 1
            index -= 1
        return index

    index_s, index_t = len(s) - 1, len(t) - 1
    while index_s >= 0 or index_t >= 0:
        index_s = next_valid_char(s, index_s)
        index_t = next_valid_char(t, index_t)

        char_s = s[index_s] if index_s >= 0 else ""
        char_t = t[index_t] if index_t >= 0 else ""
        if char_s != char_t:
            return False
        index_s -= 1
        index_t -= 1

    return True
    # Time: O(n + m) n = length of s and m = length of t 
    # Space: O(1)


def main():
    result = backspace_compare(s = "ab#c", t = "ad#c")
    print(result) # True

    result = backspace_compare(s = "ab##", t = "c#d#")
    print(result) # True

    result = backspace_compare(s = "a#c", t = "b")
    print(result) # False

if __name__ == "__main__":
    main()

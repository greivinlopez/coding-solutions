# ----------------------------
# 696. Count Binary Substrings
# ----------------------------

# Problem: https://leetcode.com/problems/count-binary-substrings
#
# Given a binary string s, return the number of non-empty substrings that have the
# same number of 0's and 1's, and all the 0's and all the 1's in these substrings
# are grouped consecutively.
# 
# Substrings that occur multiple times are counted the number of times they occur.
# 
# Example 1:
# 
# Input: s = "00110011"
# Output: 6
# 
# Explanation: There are 6 substrings that have equal number of consecutive 1's
# and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times
# they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not
# grouped together.
# 
# Example 2:
# 
# Input: s = "10101"
# Output: 4
# 
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal
# number of consecutive 1's and 0's.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s[i] is either '0' or '1'.

# Credit: Jaweria Batool -> https://github.com/Jaweria-B
def count_binary_substrings(s):
    left = 0
    right = 0
    ans = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            prev_char = s[i-1]
            curr_char = s[i]
            left = i-1
            right = i
            while left >= 0 and right < len(s) and s[left] == prev_char and s[right] == curr_char:
                if s[left] != s[right]:
                    left -= 1
                    right += 1
                    ans += 1
                else:
                    break
                    
    return ans
    # Time: O(n²)
    # Space: O(1)


def main():
    result = count_binary_substrings(s = "00110011")
    print(result) # 6

    result = count_binary_substrings(s = "10101")
    print(result) # 4

if __name__ == "__main__":
    main()

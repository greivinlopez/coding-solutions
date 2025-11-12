# ----------------------------------------------------------
# 1461. Check If A String Contains All Binary Codes Of Size K
# ----------------------------------------------------------

# Problem: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k
#
# Given a binary string s and an integer k, return true if every binary code of
# length k is a substring of s. Otherwise, return false.
# 
# Example 1:
# 
# Input: s = "00110110", k = 2
# Output: true
# Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They
# can be all found as substrings at indices 0, 1, 3 and 2 respectively.
# 
# Example 2:
# 
# Input: s = "0110", k = 1
# Output: true
# Explanation: The binary codes of length 1 are "0" and "1", it is clear that both
# exist as a substring.
# 
# Example 3:
# 
# Input: s = "0110", k = 2
# Output: false
# Explanation: The binary code "00" is of length 2 and does not exist in the
# array.
# 
# 
# Constraints:
#         1 <= s.length <= 5 * 10^5
#         s[i] is either '0' or '1'.
#         1 <= k <= 20


# Solution: https://youtu.be/qU32rTy_kOM
# Credit: Navdeep Singh founder of NeetCode
def has_all_codes(s, k):
    return len(set(s[i : i + k] for i in range(len(s) - k + 1))) == 2**k


def main():
    result = has_all_codes(s = "00110110", k = 2)
    print(result) # True

    result = has_all_codes(s = "0110", k = 1)
    print(result) # True

    result = has_all_codes(s = "0110", k = 2)
    print(result) # False

if __name__ == "__main__":
    main()

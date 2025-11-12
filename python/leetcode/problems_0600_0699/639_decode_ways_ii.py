# -------------------
# 639. Decode Ways II
# -------------------

# Problem: https://leetcode.com/problems/decode-ways-ii
#
# A message containing letters from A-Z can be encoded into numbers using the
# following mapping:
# 
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# 
# To decode an encoded message, all the digits must be grouped then mapped back
# into letters using the reverse of the mapping above (there may be multiple
# ways). For example, "11106" can be mapped into:
#  
#        "AAJF" with the grouping (1 1 10 6)
#        "KJF" with the grouping (11 10 6)
# 
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
# 'F' since "6" is different from "06".
# 
# In addition to the mapping above, an encoded message may contain the '*'
# character, which can represent any digit from '1' to '9' ('0' is excluded). For
# example, the encoded message "1*" may represent any of the encoded messages
# "11", "12", "13", "14", "15", "16", "17", "18", or "19". Decoding "1*" is
# equivalent to decoding any of the encoded messages it can represent.
# 
# Given a string s consisting of digits and '*' characters, return the number of
# ways to decode it.
# 
# Since the answer may be very large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: s = "*"
# Output: 9
# 
# Explanation: The encoded message can represent any of the encoded messages "1",
# "2", "3", "4", "5", "6", "7", "8", or "9".
# Each of these can be decoded to the strings "A", "B", "C", "D", "E", "F", "G",
# "H", and "I" respectively.
# Hence, there are a total of 9 ways to decode "*".
# 
# Example 2:
# 
# Input: s = "1*"
# Output: 18
# 
# Explanation: The encoded message can represent any of the encoded messages "11",
# "12", "13", "14", "15", "16", "17", "18", or "19".
# Each of these encoded messages have 2 ways to be decoded (e.g. "11" can be
# decoded to "AA" or "K").
# Hence, there are a total of 9 * 2 = 18 ways to decode "1*".
# 
# Example 3:
# 
# Input: s = "2*"
# Output: 15
# 
# Explanation: The encoded message can represent any of the encoded messages "21",
# "22", "23", "24", "25", "26", "27", "28", or "29".
# "21", "22", "23", "24", "25", and "26" have 2 ways of being decoded, but "27",
# "28", and "29" only have 1 way.
# Hence, there are a total of (6 * 2) + (3 * 1) = 12 + 3 = 15 ways to decode "2*".
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s[i] is a digit or '*'.


# Solution: https://algo.monster/liteproblems/639
# Credit: AlgoMonster
def num_decodings(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # Dynamic programming with space optimization
    # prev_prev: number of ways to decode up to position i-2
    # prev: number of ways to decode up to position i-1  
    # curr: number of ways to decode up to position i
    prev_prev, prev, curr = 0, 1, 0
    
    for i in range(1, n + 1):
        # Single digit decoding (using character at position i-1)
        if s[i - 1] == "*":
            # '*' can represent any digit from 1 to 9
            curr = (9 * prev) % MOD
        elif s[i - 1] != "0":
            # Non-zero digit can be decoded as itself
            curr = prev
        else:
            # '0' cannot be decoded as a single digit
            curr = 0
        
        # Two-digit decoding (using characters at positions i-2 and i-1)
        if i > 1:
            if s[i - 2] == "*" and s[i - 1] == "*":
                # "**" can represent: 11-19 (9 ways) and 21-26 (6 ways)
                curr = (curr + 15 * prev_prev) % MOD
            elif s[i - 2] == "*":
                # "*X" where X is a digit
                if s[i - 1] > "6":
                    # Only "1X" is valid (X > 6), so 1 way
                    curr = (curr + prev_prev) % MOD
                else:
                    # Both "1X" and "2X" are valid (X <= 6), so 2 ways
                    curr = (curr + 2 * prev_prev) % MOD
            elif s[i - 1] == "*":
                # "X*" where X is a digit
                if s[i - 2] == "1":
                    # "1*" can represent 11-19, so 9 ways
                    curr = (curr + 9 * prev_prev) % MOD
                elif s[i - 2] == "2":
                    # "2*" can represent 21-26, so 6 ways
                    curr = (curr + 6 * prev_prev) % MOD
            else:
                # Both are regular digits
                # Check if they form a valid two-digit number (10-26)
                if s[i - 2] != "0":
                    two_digit_value = int(s[i - 2]) * 10 + int(s[i - 1])
                    if two_digit_value <= 26:
                        curr = (curr + prev_prev) % MOD
        
        # Shift values for next iteration
        prev_prev, prev = prev, curr
    
    return curr
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_decodings(s = "*")
    print(result) # 9

    result = num_decodings(s = "1*")
    print(result) # 18

    result = num_decodings(s = "2*")
    print(result) # 15

if __name__ == "__main__":
    main()

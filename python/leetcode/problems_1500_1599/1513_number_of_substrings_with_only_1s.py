# ---------------------------------------
# 1513. Number of Substrings With Only 1s
# ---------------------------------------

# Problem: https://leetcode.com/problems/number-of-substrings-with-only-1s
#
# Given a binary string s, return the number of substrings with all characters
# 1's. Since the answer may be too large, return it modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: s = "0110111"
# Output: 9
# 
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.
# 
# Example 2:
# 
# Input: s = "101"
# Output: 2
# 
# Explanation: Substring "1" is shown 2 times in s.
# 
# Example 3:
# 
# Input: s = "111111"
# Output: 21
# 
# Explanation: Each substring contains only 1's characters.
# 
# 
# Constraints:
#         1 <= s.length <= 10⁵
#         s[i] is either '0' or '1'.


# Solution: https://algo.monster/liteproblems/1513
# Credit: AlgoMonster
def num_sub(s):
    MOD = 10**9 + 7
    total_count = 0  # Total number of valid substrings
    consecutive_ones = 0  # Length of current consecutive '1's sequence
    
    # Iterate through each character in the string
    for char in s:
        if char == "1":
            # Extend the current sequence of '1's
            consecutive_ones += 1
            # Add all substrings ending at current position
            # (consecutive_ones represents how many valid substrings end here)
            total_count += consecutive_ones
        else:
            # Reset counter when we encounter '0'
            consecutive_ones = 0
    
    # Return result modulo 10^9 + 7 to prevent overflow
    return total_count % MOD
    # Time: O(n)
    # Space: O(1)


def main():
    result = num_sub(s = "0110111")
    print(result) # 9

    result = num_sub(s = "101")
    print(result) # 2

    result = num_sub(s = "111111")
    print(result) # 21

if __name__ == "__main__":
    main()

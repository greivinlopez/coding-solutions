# -------------------------------------------------------
# 1758. Minimum Changes To Make Alternating Binary String
# -------------------------------------------------------

# Problem: https://leetcode.com/problems/merge-strings-alternately
#
# You are given a string s consisting only of the characters '0' and '1'. In one 
# operation, you can change any '0' to '1' or vice versa.
# 
# The string is called alternating if no two adjacent characters are equal. For 
# example, the string "010" is alternating, while the string "0100" is not.
# 
# Return the minimum number of operations needed to make s alternating.
#  
# Example 1:
# 
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:
# 
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:
# 
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
#  
# 
# Constraints:
#       1 <= s.length <= 10^4
#       s[i] is either '0' or '1'.


# Solution: https://youtu.be/9vAQdmVU2ds
# Credit: Navdeep Singh founder of NeetCode
def min_operations(s):
    count = 0 # operations if s start w 0

    for i in range(len(s)):
        if i % 2: # odd
            count += 1 if s[i] == "0" else 0
        else: # even
            count += 1 if s[i] == "1" else 0
    
    return min(count, len(s) - count)


def main():
    result = min_operations("0100")
    print(result) # 1

    result = min_operations("10")
    print(result) # 0

    result = min_operations("1111")
    print(result) # 2

if __name__ == "__main__":
    main()

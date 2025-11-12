# -------------------------------
# 2864. Maximum Odd Binary Number
# -------------------------------

# Problem: https://leetcode.com/problems/maximum-odd-binary-number
#
# You are given a binary string s that contains at least one '1'.
# 
# You have to rearrange the bits in such a way that the resulting binary number is
# the maximum odd binary number that can be created from this combination.
# 
# Return a string representing the maximum odd binary number that can be created
# from the given combination.
# 
# Note that the resulting string can have leading zeros.
# 
# Example 1:
# 
# Input: s = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So
# the answer is "001".
# 
# Example 2:
# 
# Input: s = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number
# that can be made with the remaining digits is "100". So the answer is "1001".
# 
# 
# Constraints:
#         1 <= s.length <= 100
#         s consists only of '0' and '1'.
#         s contains at least one '1'.


# Solution: https://youtu.be/EUKLOAv4-IQ
# Credit: Navdeep Singh founder of NeetCode
def maximum_odd_binary_number(s):
    # Count 1s and build at end
    count = 0
    for c in s:
        if c == "1":
            count += 1
    
    return (count - 1) * "1" + (len(s) - count) * "0" + "1"

def maximum_odd_binary_number_alt(s):
    # Traverse and swap indices
    s = [c for c in s]
    left = 0

    for i in range(len(s)):
        if s[i] == "1":
            s[i], s[left] = s[left], s[i]
            left += 1
    s[left - 1], s[len(s) - 1] = s[len(s) - 1], s[left - 1]
    return "".join(s)


def main():
    result = maximum_odd_binary_number("010")
    print(result) # "001"

    result = maximum_odd_binary_number("0101")
    print(result) # "1001"

if __name__ == "__main__":
    main()

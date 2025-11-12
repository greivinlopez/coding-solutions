# ----------------------------------
# 1903. Largest Odd Number in String
# ----------------------------------

# Problem: https://leetcode.com/problems/largest-odd-number-in-string
#
# You are given a string num, representing a large integer. Return the largest-
# valued odd integer (as a string) that is a non-empty substring of num, or an
# empty string "" if no odd integer exists.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# Example 1:
# 
# Input: num = "52"
# Output: "5"
# 
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the
# only odd number.
# 
# Example 2:
# 
# Input: num = "4206"
# Output: ""
# 
# Explanation: There are no odd numbers in "4206".
# 
# Example 3:
# 
# Input: num = "35427"
# Output: "35427"
# 
# Explanation: "35427" is already an odd number.
# 
# 
# Constraints:
#         1 <= num.length <= 10^5
#         num only consists of digits and does not contain any leading zeros.


# Solution: https://youtu.be/svuPjFAUeDE
# Credit: Navdeep Singh founder of NeetCode
def largest_odd_number(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2:
            return num[:i + 1]
    return ""
    # Time: O(n)
    # Space: O(1)


def main():
    result = largest_odd_number(num = "52")
    print(result) # "5"

    result = largest_odd_number(num = "4206")
    print(result) # ""

    result = largest_odd_number(num = "35427")
    print(result) # "35427"

if __name__ == "__main__":
    main()

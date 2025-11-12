# --------------------
# 402. Remove K Digits
# --------------------

# Problem: https://leetcode.com/problems/remove-k-digits/
# 
# Given string num representing a non-negative integer num, and an integer k, 
# return the smallest possible integer after removing k digits from num.
# 
#  
# Example 1:
# 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 
# which is the smallest.
# 
# 
# Example 2:
# 
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# 
# 
# Example 3:
# 
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
# 
# 
# Constraints:
# 
# 	1 <= k <= num.length <= 105
# 	num consists of only digits.
# 	num does not have any leading zeros except for the zero itself.


# Solution: https://youtu.be/cFabMOnJaq0
# Credit: Navdeep Singh founder of NeetCode
def remove_k_digits(num, k):
    stack = []
    for i in num:
        while stack and stack[-1] > i and k > 0:
            k -= 1
            stack.pop()
        if stack or i != "0":
            stack.append(i)
    if k:
        stack = stack[:-k]
    return ''.join(stack) or '0'


def main():
    result = remove_k_digits(num = "1432219", k = 3)
    print(result) # "1219"

    result = remove_k_digits(num = "10200", k = 1)
    print(result) # "200"

    result = remove_k_digits(num = "10", k = 2)
    print(result) # "0"

if __name__ == "__main__":
    main()

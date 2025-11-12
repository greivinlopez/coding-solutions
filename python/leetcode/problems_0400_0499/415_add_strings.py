# ----------------
# 415. Add Strings
# ----------------

# Problem: https://leetcode.com/problems/add-strings
#
# Given two non-negative integers, num1 and num2 represented as string, return the
# sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large
# integers (such as BigInteger). You must also not convert the inputs to integers
# directly.
# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"
# Constraints:
#         1 <= num1.length, num2.length <= 104
#         num1 and num2 consist of only digits.
#         num1 and num2 don't have any leading zeros except for the zero itself.


# Solution: https://leetcode.com/problems/add-strings/solutions/436345/python3-easy-code-with-one-loop-guides-provided
def add_strings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = []
    carry = i = 0
    l1 , l2 = len(num1), len(num2)
    l3 = max(l1, l2)
    while i < l3 or carry:
        dig1 = (ord(num1[i]) - ord('0')) if i < l1 else 0
        dig2 = (ord(num2[i]) - ord('0')) if i < l2 else 0
        sm = ((dig1 + dig2 + carry) % 10)
        carry = ((dig1 + dig2 + carry) // 10)
        result.append(str(sm))
        i += 1
    return ''.join(result[::-1])


def main():
    result = add_strings(num1 = "11", num2 = "123")
    print(result) # "134"

    result = add_strings(num1 = "456", num2 = "77")
    print(result) # "533"

    result = add_strings(num1 = "0", num2 = "0")
    print(result) # "0"

if __name__ == "__main__":
    main()

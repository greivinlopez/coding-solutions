# -------------------------------------
# 357. Count Numbers with Unique Digits
# -------------------------------------

# Problem: https://leetcode.com/problems/count-numbers-with-unique-digits
#
# Given an integer n, return the count of all numbers with unique digits, x, where
# 0 <= x < 10ⁿ.
# 
# Example 1:
# 
# Input: n = 2
# Output: 91
# 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
# excluding 11,22,33,44,55,66,77,88,99
# 
# Example 2:
# 
# Input: n = 0
# Output: 1
# 
# 
# Constraints:
#         0 <= n <= 8


# Solution: https://leetcode.com/problems/count-numbers-with-unique-digits/solutions/4944371/math-beats-100-00-simple-code-explanation-python-c-c-java
# Credit: https://leetcode.com/u/Wynder/
def count_numbers_with_unique_digits(n):
    if n == 0: return 1
    total = 10
    prod = 9
    for i in range(2, n + 1):
        total += prod * (11 - i)
        prod *= 11 - i
    return total
    # Time: O(n)
    # Space: O(1)


def main():
    result = count_numbers_with_unique_digits(2)
    print(result) # 91

    result = count_numbers_with_unique_digits(0)
    print(result) # 1

if __name__ == "__main__":
    main()

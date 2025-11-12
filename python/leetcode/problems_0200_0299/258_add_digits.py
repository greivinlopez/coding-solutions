# ---------------
# 258. Add Digits
# ---------------

# Problem: https://leetcode.com/problems/add-digits
#
# Given an integer num, repeatedly add all its digits until the result has only
# one digit, and return it.
# 
# Example 1:
# 
# Input: num = 38
# Output: 2
# 
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.
# 
# Example 2:
# 
# Input: num = 0
# Output: 0
# 
# 
# Constraints:
#         0 <= num <= 2³¹ - 1
# 
# Follow up: Could you do it without any loop/recursion in O(1) runtime?


# Solution: https://leetcode.com/problems/add-digits/solutions/5412232/python-100-beat-100-efficient-optimal-solution-easy-to-understand
# Credit: Adit Gaur -> https://leetcode.com/u/Adit_gaur/
def add_digits_alt(num):
    if num == 0 : return 0
    if num % 9 == 0 : return 9
    else : return (num % 9) 
    # Time: O(1)
    # Space: O(1)

# Optimal Solution: https://leetcodethehardway.com/solutions/0200-0299/add-digits-easy#approach-2-congruence-formula
def add_digits(num):
    return (1 + (num - 1)) % 9 
    # Time: O(1)
    # Space: O(1)


def main():
    result = add_digits(38)
    print(result) # 2

    result = add_digits(0)
    print(result) # 0

if __name__ == "__main__":
    main()

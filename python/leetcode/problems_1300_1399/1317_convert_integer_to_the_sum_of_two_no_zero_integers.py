# --------------------------------------------------------
# 1317. Convert Integer to the Sum of Two No-Zero Integers
# --------------------------------------------------------

# Problem: https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers
#
# No-Zero integer is a positive integer that does not contain any 0 in its decimal
# representation.
# 
# Given an integer n, return a list of two integers [a, b] where:
# 
#         a and b are No-Zero integers.
#         a + b = n
# 
# The test cases are generated so that there is at least one valid solution. If
# there are many valid solutions, you can return any of them.
# 
# Example 1:
# 
# Input: n = 2
# Output: [1,1]
# 
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# 
# Example 2:
# 
# Input: n = 11
# Output: [2,9]
# 
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
# 
# 
# Constraints:
#         2 <= n <= 10⁴


# Solution: https://algo.monster/liteproblems/1317
# Credit: AlgoMonster
def get_no_zero_integers(n):
    # Iterate through all possible values for the first integer
    for first_num in range(1, n):
        # Calculate the second integer to make the sum equal to n
        second_num = n - first_num
        
        # Convert both numbers to strings and concatenate them
        combined_str = str(first_num) + str(second_num)
        
        # Check if the digit '0' appears in either number
        if '0' not in combined_str:
            # Return the valid pair as soon as we find one
            return [first_num, second_num]
    # Time: O(n * log n)
    # Space: O(log n)


def main():
    result = get_no_zero_integers(n = 2)
    print(result) # [1, 1]

    result = get_no_zero_integers(n = 11)
    print(result) # [2, 9]

if __name__ == "__main__":
    main()

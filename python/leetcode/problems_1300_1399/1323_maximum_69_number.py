# -----------------------
# 1323. Maximum 69 Number
# -----------------------

# Problem: https://leetcode.com/problems/maximum-69-number
#
# You are given a positive integer num consisting only of digits 6 and 9.
# 
# Return the maximum number you can get by changing at most one digit (6 becomes
# 9, and 9 becomes 6).
# 
# Example 1:
# 
# Input: num = 9669
# Output: 9969
# 
# Explanation:
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# 
# Example 2:
# 
# Input: num = 9996
# Output: 9999
# 
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# 
# Example 3:
# 
# Input: num = 9999
# Output: 9999
# 
# Explanation: It is better not to apply any change.
# 
# 
# Constraints:
#         1 <= num <= 10⁴
#         num consists of only 6 and 9 digits.


# Solution: https://algo.monster/liteproblems/1323
# Credit: AlgoMonster
def maximum_69_number(num):
    # Convert the number to string for easier manipulation
    num_str = str(num)
    
    # Replace the first occurrence of '6' with '9' to maximize the number
    # The replace method with count=1 ensures only the first '6' is replaced
    # This gives us the maximum possible value since replacing the leftmost '6'
    # with '9' yields the largest increase
    modified_str = num_str.replace("6", "9", 1)
    
    # Convert the modified string back to integer and return
    return int(modified_str)
    # Time: O(log n)
    # Space: O(log n)
    # n = num

# Can be simplified as: return int(str(num).replace('6', '9', 1))

def main():
    result = maximum_69_number(9669)
    print(result) # 9969

    result = maximum_69_number(9996)
    print(result) # 9999

    result = maximum_69_number(9999)
    print(result) # 9999

if __name__ == "__main__":
    main()

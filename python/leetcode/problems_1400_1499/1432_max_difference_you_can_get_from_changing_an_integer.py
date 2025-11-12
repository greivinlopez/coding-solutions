# ---------------------------------------------------------
# 1432. Max Difference You Can Get From Changing an Integer
# ---------------------------------------------------------

# Problem: https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer
#
# You are given an integer num. You will apply the following steps to num two
# separate times:
#         
#   * Pick a digit x (0 <= x <= 9).
#   * Pick another digit y (0 <= y <= 9). Note y can be equal to x.
#   * Replace all the occurrences of x in the decimal representation of num by y.
# 
# Let a and b be the two results from applying the operation to num independently.
# 
# Return the max difference between a and b.
# 
# Note that neither a nor b may have any leading zeros, and must not be 0.
# 
# Example 1:
# 
# Input: num = 555
# Output: 888
# 
# Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
# The second time pick x = 5 and y = 1 and store the new integer in b.
# We have now a = 999 and b = 111 and max difference = 888
# 
# Example 2:
# 
# Input: num = 9
# Output: 8
# 
# Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
# The second time pick x = 9 and y = 1 and store the new integer in b.
# We have now a = 9 and b = 1 and max difference = 8
# 
# 
# Constraints:
#         1 <= num <= 10⁸


# Solution: https://algo.monster/liteproblems/1432
# Credit: AlgoMonster
def max_diff(num):
    # Convert number to string for digit manipulation
    max_num_str = str(num)
    min_num_str = str(num)
    
    # To maximize: replace first non-9 digit with 9
    for digit in max_num_str:
        if digit != '9':
            # Replace all occurrences of this digit with 9
            max_num_str = max_num_str.replace(digit, '9')
            break
    
    # To minimize: apply different strategies based on first digit
    if min_num_str[0] != '1':
        # If first digit is not 1, replace all occurrences with 1
        min_num_str = min_num_str.replace(min_num_str[0], '1')
    else:
        # If first digit is 1, find first digit (after position 0) 
        # that is not 0 or 1, and replace with 0
        for digit in min_num_str[1:]:
            if digit not in '01':
                min_num_str = min_num_str.replace(digit, '0')
                break
    
    # Calculate and return the difference
    max_value = int(max_num_str)
    min_value = int(min_num_str)
    return max_value - min_value
    # Time: O(log num)
    # Space: O(log num)


def main():
    result = max_diff(num = 555)
    print(result) # 888

    result = max_diff(num = 9)
    print(result) # 8

if __name__ == "__main__":
    main()

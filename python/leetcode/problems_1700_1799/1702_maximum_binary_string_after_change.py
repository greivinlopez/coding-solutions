# ----------------------------------------
# 1702. Maximum Binary String After Change
# ----------------------------------------

# Problem: https://leetcode.com/problems/maximum-binary-string-after-change
#
# You are given a binary string binary consisting of only 0's or 1's. You can
# apply each of the following operations any number of times:
#         
#   * Operation 1: If the number contains the substring "00", you can replace
#     it with "10".
#       * For example, "00010" -> "10010"
#   * Operation 2: If the number contains the substring "10", you can replace
#     it with "01".
#       * For example, "00010" -> "00001"
# 
# Return the maximum binary string you can obtain after any number of operations.
# 
# Binary string x is greater than binary string y if x's decimal representation is
# greater than y's decimal representation.
# 
# Example 1:
# 
# Input: binary = "000110"
# Output: "111011"
# 
# Explanation: A valid transformation sequence can be:
# "000110" -> "000101"
# "000101" -> "100101"
# "100101" -> "110101"
# "110101" -> "110011"
# "110011" -> "111011"
# 
# Example 2:
# 
# Input: binary = "01"
# Output: "01"
# 
# Explanation: "01" cannot be transformed any further.
# 
# 
# Constraints:
#         1 <= binary.length <= 10⁵
#         binary consist of '0' and '1'.


# Solution: https://algo.monster/liteproblems/1702
# Credit: AlgoMonster
def maximum_binary_string(binary):
    # Find the index of the first '0' in the binary string
    first_zero_index = binary.find('0')
    
    # If there are no zeros, the string is already maximum (all ones)
    if first_zero_index == -1:
        return binary
    
    # Count the number of zeros after the first zero
    # This determines where the single '0' will be placed in the result
    zeros_after_first = binary[first_zero_index + 1:].count('0')
    
    # Calculate the position where the single '0' will be placed
    # The position is: first_zero_index + number_of_zeros_after_first
    zero_position = first_zero_index + zeros_after_first
    
    # Construct the maximum binary string:
    # - All '1's before the zero position
    # - A single '0' at the calculated position
    # - All '1's after the zero position
    result = '1' * zero_position + '0' + '1' * (len(binary) - zero_position - 1)
    
    return result
    # Time: O(n)
    # Space: O(n)


def main():
    result = maximum_binary_string(binary = "000110")
    print(result) # "111011"

    result = maximum_binary_string(binary = "01")
    print(result) # "01"

if __name__ == "__main__":
    main()

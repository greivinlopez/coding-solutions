# --------------------------------------
# 1573. Number of Ways to Split a String
# --------------------------------------

# Problem: https://leetcode.com/problems/number-of-ways-to-split-a-string
#
# Given a binary string s, you can split s into 3 non-empty strings s1, s2, and s3
# where s1 + s2 + s3 = s.
# 
# Return the number of ways s can be split such that the number of ones is the
# same in s1, s2, and s3. Since the answer may be too large, return it 
# modulo 10⁹ + 7.
# 
# Example 1:
# 
# Input: s = "10101"
# Output: 4
# 
# Explanation: There are four ways to split s in 3 parts where each part contain
# the same number of letters '1'.
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
# 
# Example 2:
# 
# Input: s = "1001"
# Output: 0
# 
# Example 3:
# 
# Input: s = "0000"
# Output: 3
# 
# Explanation: There are three ways to split s in 3 parts.
# "0|0|00"
# "0|00|0"
# "00|0|0"
# 
# 
# Constraints:
#         3 <= s.length <= 10⁵
#         s[i] is either '0' or '1'.


# Solution: 
# Credit: Navdeep Singh founder of NeetCode
def num_ways(s):
    
    def find_position_of_nth_one(target_count):
        ones_seen = 0
        for index, char in enumerate(s):
            ones_seen += int(char == '1')
            if ones_seen == target_count:
                return index
        return -1  # Should not reach here if target_count is valid
    
    # Count total number of 1s and check if divisible by 3
    total_ones = sum(char == '1' for char in s)
    ones_per_part, remainder = divmod(total_ones, 3)
    
    # If not divisible by 3, impossible to split equally
    if remainder != 0:
        return 0
    
    string_length = len(s)
    MOD = 10**9 + 7
    
    # Special case: no 1s in the string (all zeros)
    if ones_per_part == 0:
        # Can place 2 dividers among (n-1) positions
        # Number of ways = C(n-1, 2) = (n-1)*(n-2)/2
        return ((string_length - 1) * (string_length - 2) // 2) % MOD
    
    # Find boundaries for valid split positions
    # First split can be placed after ones_per_part 1s until before (ones_per_part+1)th 1
    first_part_end = find_position_of_nth_one(ones_per_part)
    second_part_start = find_position_of_nth_one(ones_per_part + 1)
    
    # Second split can be placed after 2*ones_per_part 1s until before (2*ones_per_part+1)th 1
    second_part_end = find_position_of_nth_one(ones_per_part * 2)
    third_part_start = find_position_of_nth_one(ones_per_part * 2 + 1)
    
    # Count valid positions for each split
    first_split_options = second_part_start - first_part_end
    second_split_options = third_part_start - second_part_end
    
    # Total ways is product of options for each split
    return (first_split_options * second_split_options) % MOD
    # Time: O(n)
    # Space: O(n)


def main():
    result = num_ways(s = "10101")
    print(result) # 4

    result = num_ways(s = "1001")
    print(result) # 0

    result = num_ways(s = "0000")
    print(result) # 3

if __name__ == "__main__":
    main()

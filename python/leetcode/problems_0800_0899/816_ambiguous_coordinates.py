# --------------------------
# 816. Ambiguous Coordinates
# --------------------------

# Problem: https://leetcode.com/problems/ambiguous-coordinates
#
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we
# removed all commas, decimal points, and spaces and ended up with the string s.
#         
#   * For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
# 
# Return a list of strings representing all possibilities for what our original
# coordinates could have been.
# 
# Our original representation never had extraneous zeroes, so we never started
# with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other
# number that can be represented with fewer digits. Also, a decimal point within a
# number never occurs without at least one digit occurring before it, so we never
# started with numbers like ".1".
# 
# The final answer list can be returned in any order. All coordinates in the final
# answer have exactly one space between them (occurring after the comma.)
# 
# Example 1:
# 
# Input: s = "(123)"
# Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
# 
# Example 2:
# 
# Input: s = "(0123)"
# Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12,
# 3)"]
# 
# Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
# 
# Example 3:
# 
# Input: s = "(00011)"
# Output: ["(0, 0.011)","(0.001, 1)"]
# 
# 
# Constraints:
#         4 <= s.length <= 12
#         s[0] == '(' and s[s.length - 1] == ')'.
#         The rest of s are digits.


# Solution: https://algo.monster/liteproblems/816
# Credit: AlgoMonster
def ambiguous_coordinates(s):
    def generate_valid_numbers(start, end):
        valid_numbers = []
        
        # Try all possible positions for decimal point
        for decimal_pos in range(1, end - start + 1):
            # Split into integer part and decimal part
            integer_part = s[start:start + decimal_pos]
            decimal_part = s[start + decimal_pos:end]
            
            # Check validity conditions:
            # 1. Integer part should not have leading zeros (unless it's just "0")
            # 2. Decimal part should not have trailing zeros
            has_valid_integer = (integer_part == '0' or not integer_part.startswith('0'))
            has_valid_decimal = not decimal_part.endswith('0')
            
            if has_valid_integer and has_valid_decimal:
                # Add decimal point only if there's a decimal part
                if decimal_pos < end - start:
                    number = integer_part + '.' + decimal_part
                else:
                    number = integer_part
                valid_numbers.append(number)
        
        return valid_numbers
    
    # Remove parentheses from input string
    string_length = len(s)
    result = []
    
    # Try all possible positions to split into two coordinates
    for split_pos in range(2, string_length - 1):
        # Generate all valid numbers for first coordinate
        first_coordinate_options = generate_valid_numbers(1, split_pos)
        # Generate all valid numbers for second coordinate
        second_coordinate_options = generate_valid_numbers(split_pos, string_length - 1)
        
        # Create all combinations of valid coordinates
        for x in first_coordinate_options:
            for y in second_coordinate_options:
                result.append(f'({x}, {y})')
    
    return result
    # Time: O(n⁴)
    # Space: O(n³)


def main():
    result = ambiguous_coordinates(s = "(123)")
    print(result) # ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]

    result = ambiguous_coordinates(s = "(0123)")
    print(result) # ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]

    result = ambiguous_coordinates(s = "(00011)")
    print(result) # ["(0, 0.011)","(0.001, 1)"]

if __name__ == "__main__":
    main()

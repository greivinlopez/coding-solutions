# ------------------------
# 1556. Thousand Separator
# ------------------------

# Problem: https://leetcode.com/problems/thousand-separator
#
# Given an integer n, add a dot (".") as the thousands separator and return it in
# string format.
# 
# Example 1:
# 
# Input: n = 987
# Output: "987"
# 
# Example 2:
# 
# Input: n = 1234
# Output: "1.234"
# 
# 
# Constraints:
#         0 <= n <= 2³¹ - 1


# Solution: https://algo.monster/liteproblems/1556
# Credit: AlgoMonster
def thousand_separator(n):
    # Counter to track digits processed in current group (groups of 3)
    digit_count = 0
    # List to build the result string from right to left
    result = []
    
    # Process digits from right to left
    while True:
        # Extract the rightmost digit using divmod
        n, digit = divmod(n, 10)
        
        # Add the current digit to result
        result.append(str(digit))
        digit_count += 1
        
        # If no more digits left, exit the loop
        if n == 0:
            break
        
        # After every 3 digits, add a thousand separator
        if digit_count == 3:
            result.append('.')
            digit_count = 0  # Reset counter for next group
    
    # Reverse the result since we built it backwards
    return ''.join(result[::-1])
    # Time: O(d). d ≈ log n
    # Space: O(d)
    # d = the number of digits in the integer n.

# One liner solution
# Solution: https://leetcode.com/problems/thousand-separator/solutions/805712/python3-1-line-by-ye15-2u35
# Credit: Ye Gao -> https://leetcode.com/u/ye15/
def thousand_separator_short(n):
    return f"{n:,}".replace(",", ".")
    # Time: O(d). d ≈ log n
    # Space: O(d)
    # d = the number of digits in the integer n.


def main():
    result = thousand_separator(n = 987)
    print(result) # "987"

    result = thousand_separator(n = 1234)
    print(result) # "1.234"

if __name__ == "__main__":
    main()

# ------------------------------
# 171. Excel Sheet Column Number
# ------------------------------

# Problem: https://leetcode.com/problems/excel-sheet-column-number
#
# Given a string columnTitle that represents the column title as appears in an
# Excel sheet, return its corresponding column number.
# 
# For example:
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# 
# Example 1:
# 
# Input: columnTitle = "A"
# Output: 1
# 
# Example 2:
# 
# Input: columnTitle = "AB"
# Output: 28
# 
# Example 3:
# 
# Input: columnTitle = "ZY"
# Output: 701
# 
# 
# Constraints:
#         1 <= columnTitle.length <= 7
#         columnTitle consists only of uppercase English letters.
#         columnTitle is in the range ["A", "FXSHRXW"].


# My Solution
def title_to_number(columnTitle):
    n = len(columnTitle)
    res = 0
    for i in range(n):
        res = res * 26 + ord(columnTitle[i]) - 64
    return res
    # Time: O(n)
    # Space: O(1)


def main():
    result = title_to_number("A")
    print(result) # 1

    result = title_to_number("AB")
    print(result) # 28

    result = title_to_number("ZY")
    print(result) # 701

if __name__ == "__main__":
    main()

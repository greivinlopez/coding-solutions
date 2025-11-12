# -----------------------------
# 168. Excel Sheet Column Title
# -----------------------------

# Problem: https://leetcode.com/problems/excel-sheet-column-title/
# 
# Given an integer columnNumber, return its corresponding column title as it 
# appears in an Excel sheet.
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
#  
# Example 1:
# 
# Input: columnNumber = 1
# Output: "A"
# 
# 
# Example 2:
# 
# Input: columnNumber = 28
# Output: "AB"
# 
# 
# Example 3:
# 
# Input: columnNumber = 701
# Output: "ZY"
# 
# 
# Constraints:
# 
# 	1 <= columnNumber <= 231 - 1


# Solution: https://youtu.be/X_vJDpCCuoA
# Credit: Navdeep Singh founder of NeetCode
def convert_to_title(columnNumber):
    # Time: O(logn) - Log base 26 of n
    res = ""
    while columnNumber > 0:
        remainder = (columnNumber - 1) % 26
        res += chr(ord('A') + remainder)
        columnNumber = (columnNumber - 1) // 26

    return res[::-1] # reverse output


def main():
    result = convert_to_title(1)
    print(result) # "A"

    result = convert_to_title(28)
    print(result) # "AB"

    result = convert_to_title(701)
    print(result) # "ZY"

if __name__ == "__main__":
    main()

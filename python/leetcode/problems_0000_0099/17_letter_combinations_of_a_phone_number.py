# --------------------------------------------
# 17. Letter Combinations of a Phone Number ☎️
# --------------------------------------------

# Problem: https://leetcode.com/problems/letter-combinations-of-a-phone-number
#
# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png
# 
# Example 1:
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# Example 2:
# 
# Input: digits = ""
# Output: []
# 
# Example 3:
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# Constraints:
#         0 <= digits.length <= 4
#         digits[i] is a digit in the range ['2', '9'].

# Solution: https://youtu.be/0snEunUacZY
# Credit: Navdeep Singh founder of NeetCode 
def letter_combinations(digits):
    res = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i, curStr):
        if len(curStr) == len(digits):
            res.append(curStr)
            return
        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curStr + c)

    if digits:
        backtrack(0, "")

    return res
    # Time: O(4ⁿ * n)
    # Space: O(n)

# Solution: https://youtu.be/F7EoBxhPmBk
# Credit: Greg Hogg
# Almost identical
def letter_combinations_alt(digits):
    if digits == "":
        return []

    ans, sol = [], []
    
    letter_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    
    n = len(digits)

    def backtrack(i=0):
        if i == n:
            ans.append("".join(sol))
            return

        for letter in letter_map[digits[i]]:
            sol.append(letter)
            backtrack(i + 1)
            sol.pop()

    backtrack(0)
    return ans
    # Time: O(4ⁿ * n)
    # Space: O(n)

# Solution: https://leetcode.com/problems/letter-combinations-of-a-phone-number/solutions/7019849/simple-iterative-solution-in-python-no-backtracking/
# Credit: Manya Michelle -> https://leetcode.com/u/justaguy1337/
def letter_combinations_alt_2(digits):
    my_dict = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    if not digits or digits == '1':
        return []

    my_list = ['']
    for i in digits:
        temp = []
        for j in my_list:
            for k in my_dict[i]:
                temp.append(j + k)
        my_list = temp

    return my_list
    # Time: O(4ⁿ * n)
    # Space: O(n)

def main():
    result = letter_combinations("23") # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(result)
    result = letter_combinations("") # []
    print(result)
    result = letter_combinations("2") # ["a","b","c"]
    print(result)

if __name__ == "__main__":
    main()
# --------------------
# 726. Number of Atoms
# --------------------

# Problem: https://leetcode.com/problems/number-of-atoms
#
# Given a string formula representing a chemical formula, return the count of each
# atom.
# 
# The atomic element always starts with an uppercase character, then zero or more
# lowercase letters, representing the name.
# 
# One or more digits representing that element's count may follow if the count is
# greater than 1. If the count is 1, no digits will follow.
#         
#   * For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# 
# Two formulas are concatenated together to produce another formula.
#         
#   * For example, "H2O2He3Mg4" is also a formula.
# 
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.
#         
#   * For example, "(H2O2)" and "(H2O2)3" are formulas.
# 
# Return the count of all elements as a string in the following form: the first
# name (in sorted order), followed by its count (if that count is more than 1),
# followed by the second name (in sorted order), followed by its count (if that
# count is more than 1), and so on.
# 
# The test cases are generated so that all the values in the output fit in a
# 32-bit integer.
# 
# Example 1:
# 
# Input: formula = "H2O"
# Output: "H2O"
# 
# Explanation: The count of elements are {'H': 2, 'O': 1}.
# 
# Example 2:
# 
# Input: formula = "Mg(OH)2"
# Output: "H2MgO2"
# 
# Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
# 
# Example 3:
# 
# Input: formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# 
# Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
# 
# 
# Constraints:
#         1 <= formula.length <= 1000
#         formula consists of English letters, digits, '(', and ')'.
#         formula is always valid.

from collections import defaultdict

# Solution: https://youtu.be/iuK05gGBzJc
# Credit: Navdeep Singh founder of NeetCode
def count_of_atoms(formula):
    stack = [defaultdict(int)]
    i = 0
    while i < len(formula):
        if formula[i] == "(":
            stack.append(defaultdict(int))
        elif formula[i] == ")":
            cur_map = stack.pop()
            count = ""
            while i + 1 < len(formula) and formula[i+1].isdigit():
                count += formula[i+1]
                i += 1
            
            count = 1 if not count else int(count)
            prev_map = stack[-1]
            for elem in cur_map:
                prev_map[elem] += cur_map[elem] * count
        else:
            element = formula[i]
            count = ""
            if i + 1 < len(formula) and formula[i+1].islower():
                element = formula[i:i+2]
                i += 1
            
            while i + 1 < len(formula) and formula[i+1].isdigit():
                count += formula[i+1]
                i += 1
            
            count = 1 if not count else int(count)
            cur_map = stack[-1]
            cur_map[element] += count
        i += 1

    cnt_map = stack[-1]
    res = ""
    for elem in sorted(cnt_map.keys()):
        count = "" if cnt_map[elem] == 1 else cnt_map[elem]
        res += elem + str(count)
    return res
    # Time: O(n²)   n = length of the input
    # Space: O(n)


def main():
    result = count_of_atoms("H2O")
    print(result) # "H2O"

    result = count_of_atoms("Mg(OH)2")
    print(result) # "H2MgO2"

    result = count_of_atoms("K4(ON(SO3)2)2")
    print(result) # "K4N2O14S4"

if __name__ == "__main__":
    main()

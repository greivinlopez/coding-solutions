# ------------------------
# 1096. Brace Expansion II
# ------------------------

# Problem: https://leetcode.com/problems/brace-expansion-ii
#
# Under the grammar given below, strings can represent a set of lowercase words.
# Let R(expr) denote the set of words the expression represents.
# 
# The grammar can best be understood through simple examples:
#         
#   * Single letters represent a singleton set containing that word.
#
#       * R("a") = {"a"}
#       * R("w") = {"w"}
#   
#   * When we take a comma-delimited list of two or more expressions, we take
#     the union of possibilities.
#
#       * R("{a,b,c}") = {"a","b","c"}
#       * R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains 
#         each word at most once)
#         
#   * When we concatenate two expressions, we take the set of possible
#     concatenations between two words where the first word comes from the first
#     expression and the second word comes from the second expression.
#                 
#       * R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
#       * R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", 
#         "acdfh", "acefg", "acefh"}
# 
# Formally, the three rules for our grammar:
#         
#   * For every lowercase letter x, we have R(x) = {x}.
#   * For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) =
#     R(e1) ∪ R(e2) ∪ ...
#   * For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in
#     R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian
#     product.
# 
# Given an expression representing a set of words under the given grammar, return
# the sorted list of words that the expression represents.
# 
# Example 1:
# 
# Input: expression = "{a,b}{c,{d,e}}"
# Output: ["ac","ad","ae","bc","bd","be"]
# 
# Example 2:
# 
# Input: expression = "{{a,z},a{b,c},{ab,z}}"
# Output: ["a","ab","ac","z"]
# 
# Explanation: Each distinct word is written only once in the final answer.
# 
# Constraints:
#   1 <= expression.length <= 60
#   expression[i] consists of '{', '}', ','or lowercase English letters.
#   The given expression represents a set of words based on the grammar given 
#   in the description.


# Solution: https://algo.monster/liteproblems/1096
# Credit: AlgoMonster
def brace_expansion_ii(expression):
    def dfs(current_expression):
        # Find the first closing brace
        closing_brace_index = current_expression.find('}')
        
        # Base case: no more braces to expand
        if closing_brace_index == -1:
            result_set.add(current_expression)
            return
        
        # Find the matching opening brace for the first closing brace
        # Search backwards from just before the closing brace
        opening_brace_index = current_expression.rfind('{', 0, closing_brace_index - 1)
        
        # Extract parts: before the brace, inside the brace, and after the brace
        prefix = current_expression[:opening_brace_index]
        suffix = current_expression[closing_brace_index + 1:]
        brace_content = current_expression[opening_brace_index + 1:closing_brace_index]
        
        # Expand each option within the braces
        for option in brace_content.split(','):
            # Recursively process the expression with this option substituted
            dfs(prefix + option + suffix)
    
    # Initialize result set to store unique expanded strings
    result_set = set()
    
    # Start the depth-first search expansion
    dfs(expression)
    
    # Return sorted list of all unique expanded strings
    return sorted(result_set)
    # Time: O(n * 2ᵐ * m)
    # Space: O(n * 2ᵐ)


def main():
    result = brace_expansion_ii(expression = "{a,b}{c,{d,e}}")
    print(result) # ["ac","ad","ae","bc","bd","be"]

    result = brace_expansion_ii(expression = "{{a,z},a{b,c},{ab,z}}")
    print(result) # ["a","ab","ac","z"]

if __name__ == "__main__":
    main()

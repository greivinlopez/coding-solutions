# -----------------------------------------
# 990. Satisfiability of Equality Equations
# -----------------------------------------

# Problem: https://leetcode.com/problems/satisfiability-of-equality-equations
#
# You are given an array of strings equations that represent relationships between
# variables where each string equations[i] is of length 4 and takes one of two
# different forms: "xᵢ==yᵢ" or "xᵢ!=yᵢ".Here, xᵢ and yᵢ are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if it is possible to assign integers to variable names so as to
# satisfy all the given equations, or false otherwise.
# 
# Example 1:
# 
# Input: equations = ["a==b","b!=a"]
# Output: false
# 
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
# 
# Example 2:
# 
# Input: equations = ["b==a","a==b"]
# Output: true
# 
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# Constraints:
#         1 <= equations.length <= 500
#         equations[i].length == 4
#         equations[i][0] is a lowercase letter.
#         equations[i][1] is either '=' or '!'.
#         equations[i][2] is '='.
#         equations[i][3] is a lowercase letter.


# Solution: https://algo.monster/liteproblems/990
# Credit: AlgoMonster
def equations_possible(equations):

    def find(x):
        if parent[x] != x:
            # Path compression: directly connect x to its root
            parent[x] = find(parent[x])
        return parent[x]
    
    # Initialize parent array where each element is its own parent
    # Index represents character (0='a', 1='b', ..., 25='z')
    parent = list(range(26))
    
    # First pass: Process all equality equations to union equal variables
    for equation in equations:
        # Extract the two variables from the equation
        var1_index = ord(equation[0]) - ord('a')
        var2_index = ord(equation[-1]) - ord('a')
        
        # If it's an equality equation, union the two variables
        if equation[1] == '=':
            root1 = find(var1_index)
            root2 = find(var2_index)
            parent[root1] = root2
    
    # Second pass: Check all inequality equations for contradictions
    for equation in equations:
        # Extract the two variables from the equation
        var1_index = ord(equation[0]) - ord('a')
        var2_index = ord(equation[-1]) - ord('a')
        
        # If it's an inequality equation, check if variables are in same group
        if equation[1] == '!':
            if find(var1_index) == find(var2_index):
                # Contradiction: variables should be different but are in same group
                return False
    
    # All equations can be satisfied
    return True
    # Time: O(n * α(m)) ≈ O(n)
    # Space: O(1)
    # n = the number of equations
    # m = the number of elements in the disjoint set = 26
    # α = the inverse Ackermann function


def main():
    result = equations_possible(equations = ["a==b","b!=a"])
    print(result) # False

    result = equations_possible(equations = ["b==a","a==b"])
    print(result) # True

if __name__ == "__main__":
    main()

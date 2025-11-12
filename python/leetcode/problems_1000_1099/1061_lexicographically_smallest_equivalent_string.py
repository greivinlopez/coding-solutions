# --------------------------------------------------
# 1061. Lexicographically Smallest Equivalent String
# --------------------------------------------------

# Problem: https://leetcode.com/problems/lexicographically-smallest-equivalent-string
#
# You are given two strings of the same length s1 and s2 and a string baseStr.
# 
# We say s1[i] and s2[i] are equivalent characters.
#         
#   * For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', 
#     and 'c' == 'e'.
# 
# Equivalent characters follow the usual rules of any equivalence relation:
# 
#         Reflexivity: 'a' == 'a'.
#         Symmetry: 'a' == 'b' implies 'b' == 'a'.
#         Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# 
# For example, given the equivalency information from s1 = "abc" and s2 = "cde",
# "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the
# lexicographically smallest equivalent string of baseStr.
# 
# Return the lexicographically smallest equivalent string of baseStr by using the
# equivalency information from s1 and s2.
# 
# Example 1:
# 
# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# 
# Explanation: Based on the equivalency information in s1 and s2, we can group
# their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".
# 
# Example 2:
# 
# Input: s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"
# 
# Explanation: Based on the equivalency information in s1 and s2, we can group
# their characters as [h,w], [d,e,o], [l,r].
# So only the second letter 'o' in baseStr is changed to 'd', the answer is
# "hdld".
# 
# Example 3:
# 
# Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"
# 
# Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c],
# [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are
# transformed to 'a', the answer is "aauaaaaada".
# 
# 
# Constraints:
#         1 <= s1.length, s2.length, baseStr <= 1000
#         s1.length == s2.length
#         s1, s2, and baseStr consist of lowercase English letters.


# Solution: https://algo.monster/liteproblems/1061
# Credit: AlgoMonster
def smallest_equivalent_string(s1, s2, baseStr):
    
    def find(char_index):
        if parent[char_index] != char_index:
            # Path compression: directly connect to root
            parent[char_index] = find(parent[char_index])
        return parent[char_index]
    
    # Initialize parent array where each character is its own parent
    # Index 0 represents 'a', 1 represents 'b', etc.
    parent = list(range(26))
    
    # Build equivalence relationships from s1 and s2
    for char1, char2 in zip(s1, s2):
        # Convert characters to indices (0-25)
        index1 = ord(char1) - ord('a')
        index2 = ord(char2) - ord('a')
        
        # Find root parents of both characters
        root1 = find(index1)
        root2 = find(index2)
        
        # Union by rank: always attach larger root to smaller root
        # This ensures lexicographically smallest parent
        if root1 < root2:
            parent[root2] = root1
        else:
            parent[root1] = root2
    
    # Transform baseStr to its lexicographically smallest equivalent
    result_chars = []
    for char in baseStr:
        # Find the root parent (smallest equivalent character)
        char_index = ord(char) - ord('a')
        smallest_index = find(char_index)
        # Convert back to character and add to result
        result_chars.append(chr(smallest_index + ord('a')))
    
    return ''.join(result_chars)
    # Time: O(n + m)
    # Space: O(1)


def main():
    result = smallest_equivalent_string(s1 = "parker", s2 = "morris", baseStr = "parser")
    print(result) # "makkek"

    result = smallest_equivalent_string(s1 = "hello", s2 = "world", baseStr = "hold")
    print(result) # "hdld"

    result = smallest_equivalent_string(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode")
    print(result) # "aauaaaaada"

if __name__ == "__main__":
    main()
